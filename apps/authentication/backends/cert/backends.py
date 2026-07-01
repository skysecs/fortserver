# -*- coding: utf-8 -*-
#

import base64
import os
import tempfile

from django.conf import settings

from users.models import User
from common.utils import get_logger
from ..base import JMSBaseAuthBackend


__all__ = ['CertBackend']

logger = get_logger(__name__)

# SM2 曲线 OID DER 字节序列，用于判断证书算法（与 api.py 保持一致）
_SM2_OID_DER = bytes([0x06, 0x08, 0x2a, 0x81, 0x1c, 0xcf, 0x55, 0x01, 0x82, 0x2d])


class CertBackend(JMSBaseAuthBackend):
    backend = settings.AUTH_BACKEND_CERT

    @staticmethod
    def is_enabled():
        return settings.AUTH_CERT

    def authenticate(self, request, username, cert, signature, challenge):
        try:
            cert_pem = self._normalize_cert_to_pem(cert)
        except Exception as e:
            logger.warning('CertBackend: cert normalization failed: %s', e)
            return None

        if self._is_sm2_cert(cert_pem):
            return self._authenticate_sm2(cert_pem, username, signature, challenge)
        else:
            return self._authenticate_other(cert_pem, username, signature, challenge)

    # ── SM2 四步校验 ─────────────────────────────────────────────────────────

    def _authenticate_sm2(self, cert_pem, username, signature, challenge):
        # 加载证书（写临时文件 → Sm2Certificate）
        try:
            sm2_cert = self._load_sm2_cert(cert_pem)
        except Exception as e:
            logger.warning('CertBackend: failed to load SM2 cert: %s', e)
            return None

        # Step 1: 校验证书链，是否由 CA 根证书签发
        try:
            self._verify_sm2_cert_chain(sm2_cert)
        except Exception as e:
            logger.warning('CertBackend: SM2 cert chain verification failed: %s', e)
            return None

        # Step 2: 从证书 subject 提取 CN，与传入 username 比对
        cert_cn = sm2_cert.get_subject().get('commonName')
        if cert_cn != username:
            logger.warning(
                'CertBackend: cert CN %r does not match username %r', cert_cn, username
            )
            return None

        # Step 3: 用证书公钥验证签名
        public_key = sm2_cert.get_subject_public_key()
        try:
            sig_ok = self._verify_sm2_signature(public_key, signature, challenge)
        except Exception as e:
            logger.warning('CertBackend: SM2 signature verification failed: %s', e)
            return None
        if not sig_ok:
            logger.warning('CertBackend: SM2 signature mismatch')
            return None

        # Step 4: 查询并返回用户
        return User.objects.filter(username=username).first()

    @staticmethod
    def _load_sm2_cert(cert_pem):
        """将 PEM 字符串写入临时文件，加载为 Sm2Certificate 对象后立即删除临时文件。"""
        from common.utils.gmssl_python import Sm2Certificate

        fd, cert_file = tempfile.mkstemp(suffix='.crt')
        try:
            os.close(fd)
            with open(cert_file, 'w', encoding='utf-8') as f:
                f.write(cert_pem)
            sm2_cert = Sm2Certificate()
            sm2_cert.import_pem(cert_file)
        finally:
            if os.path.exists(cert_file):
                os.unlink(cert_file)
        return sm2_cert

    def _verify_sm2_cert_chain(self, sm2_cert):
        """调用 Sm2Certificate.verify_by_ca_certificate 验证证书链。"""
        from common.utils.gmssl_python import SM2_DEFAULT_ID

        ca_cert_path = getattr(settings, 'CA_CERT_FILE', '')
        if not ca_cert_path or not os.path.isfile(ca_cert_path):
            raise FileNotFoundError('CA_CERT_FILE not configured or not found')

        from common.utils.gmssl_python import Sm2Certificate
        ca_cert = Sm2Certificate()
        ca_cert.import_pem(ca_cert_path)

        if not sm2_cert.verify_by_ca_certificate(ca_cert, SM2_DEFAULT_ID):
            raise ValueError('SM2 cert chain verification failed')

    @staticmethod
    def _verify_sm2_signature(sm2_key, signature, challenge):
        """
        使用 gmssl_python 的 Sm2Signature 做 SM2withSM3 验签。

        sm2_key   : Sm2Certificate.get_subject_public_key() 返回的 Sm2Key 对象。
        signature : USB Key 返回的签名（bytes / hex 字符串 / base64 字符串，DER 格式）。
        challenge : 服务端下发的挑战码字符串；JS 端对 btoa(challenge) 做签名。
        """
        from common.utils.gmssl_python import Sm2Signature, DO_VERIFY, SM2_DEFAULT_ID

        sig_bytes = CertBackend._decode_signature(signature)

        # JS 端直接对 challenge 字符串签名，无需 base64 编码
        if isinstance(challenge, bytes):
            signed_data = challenge
        else:
            signed_data = challenge.encode('utf-8')

        verifier = Sm2Signature(sm2_key, SM2_DEFAULT_ID, DO_VERIFY)
        verifier.update(signed_data)
        return bool(verifier.verify(sig_bytes))

    # ── 工具方法 ─────────────────────────────────────────────────────────────

    @staticmethod
    def _is_sm2_cert(cert_pem):
        """通过 OID 字节序列判断证书是否使用 SM2 算法。"""
        pem_lines = cert_pem.strip().splitlines()
        b64 = ''.join(ln for ln in pem_lines if not ln.startswith('-----'))
        der = base64.b64decode(b64)
        return _SM2_OID_DER in der

    @staticmethod
    def _normalize_cert_to_pem(cert_data):
        """
        将证书统一转换为标准 PEM 格式。
        支持：已含头尾的 PEM、裸 base64 字符串、DER bytes。
        """
        if isinstance(cert_data, bytes):
            if cert_data.lstrip().startswith(b'-----BEGIN'):
                return cert_data.decode('utf-8')
            b64 = base64.b64encode(cert_data).decode('ascii')
        else:
            cert_data = cert_data.strip()
            if cert_data.startswith('-----BEGIN'):
                return cert_data
            b64 = ''.join(cert_data.split())
            base64.b64decode(b64, validate=True)  # 验证是合法 base64

        lines = [b64[i:i + 64] for i in range(0, len(b64), 64)]
        return (
            '-----BEGIN CERTIFICATE-----\n'
            + '\n'.join(lines)
            + '\n-----END CERTIFICATE-----\n'
        )

    @staticmethod
    def _decode_signature(signature):
        """
        将签名值转为 bytes。
        依次尝试：已是 bytes → 十六进制字符串 → base64 字符串。
        """
        if isinstance(signature, bytes):
            return signature
        sig = signature.strip()
        try:
            return bytes.fromhex(sig)
        except ValueError:
            pass
        try:
            return base64.b64decode(sig)
        except Exception:
            pass
        raise ValueError('Cannot decode signature: unknown format')

    # ── RSA 四步校验 ─────────────────────────────────────────────────────────

    def _authenticate_other(self, cert_pem, username, signature, challenge):
        from cryptography import x509
        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa

        # Step 1: 加载证书，判断算法类型
        try:
            cert = x509.load_pem_x509_certificate(cert_pem.encode())
        except Exception as e:
            logger.warning('CertBackend: failed to load certificate: %s', e)
            return None

        pub_key = cert.public_key()
        if isinstance(pub_key, ec.EllipticCurvePublicKey):
            logger.warning('CertBackend: ECDSA certificate verification is not supported')
            return None
        if not isinstance(pub_key, rsa.RSAPublicKey):
            logger.warning('CertBackend: unsupported key type: %s', type(pub_key).__name__)
            return None

        # Step 2: 校验证书链，是否由 CA 根证书签发
        ca_cert_path = getattr(settings, 'CA_CERT_FILE', '')
        if not ca_cert_path or not os.path.isfile(ca_cert_path):
            logger.warning('CertBackend: CA_CERT_FILE not configured or not found')
            return None
        try:
            with open(ca_cert_path, 'rb') as f:
                ca_cert = x509.load_pem_x509_certificate(f.read())
            ca_cert.public_key().verify(
                cert.signature,
                cert.tbs_certificate_bytes,
                padding.PKCS1v15(),
                cert.signature_hash_algorithm,
            )
        except InvalidSignature:
            logger.warning('CertBackend: RSA cert chain verification failed')
            return None
        except Exception as e:
            logger.warning('CertBackend: RSA cert chain verification error: %s', e)
            return None

        # Step 3: 从证书 subject 提取 CN，与传入 username 比对
        try:
            cert_cn = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
        except (IndexError, Exception):
            cert_cn = None
        if cert_cn != username:
            logger.warning(
                'CertBackend: cert CN %r does not match username %r', cert_cn, username
            )
            return None

        # Step 4: 用证书公钥验证签名（RSA PKCS1v15 + SHA256）
        sig_bytes = self._decode_signature(signature)
        signed_data = challenge if isinstance(challenge, bytes) else challenge.encode('utf-8')
        try:
            pub_key.verify(sig_bytes, signed_data, padding.PKCS1v15(), hashes.SHA256())
        except InvalidSignature:
            logger.warning('CertBackend: RSA signature mismatch')
            return None
        except Exception as e:
            logger.warning('CertBackend: RSA signature verification error: %s', e)
            return None

        # Step 5: 查询并返回用户
        return User.objects.filter(username=username).first()