<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Nền tảng PAM mã nguồn mở (máy chủ bastion)

[![][license-shield]][license-link]
[![][docs-shield]][docs-link]
[![][deepwiki-shield]][deepwiki-link]
[![][discord-shield]][discord-link]
[![][docker-shield]][docker-link]
[![][github-release-shield]][github-release-link]
[![][github-stars-shield]][github-stars-link]

[English](/README.md) · [中文(简体)](/readmes/README.zh-hans.md) · [中文(繁體)](/readmes/README.zh-hant.md) · [日本語](/readmes/README.ja.md) · [Português (Brasil)](/readmes/README.pt-br.md) · [Español](/readmes/README.es.md) · [Русский](/readmes/README.ru.md) · [한국어](/readmes/README.ko.md) · [Tiếng Việt](/readmes/README.vi.md)

</div>

<br/>

## fortserver là gì?

fortserver là nền tảng quản lý truy cập đặc quyền (PAM) mã nguồn mở có tích hợp AI. Nền tảng cung cấp cho các nhóm DevOps và CNTT một không gian làm việc thống nhất để truy cập an toàn vào SSH, RDP, Kubernetes, cơ sở dữ liệu, trang web, RemoteApp, VirtualApp và nhiều tài nguyên khác.

<img alt="Sơ đồ kiến trúc fortserver" src="assets/fortserver-architecture.png" />

## Bắt đầu nhanh

Chuẩn bị một máy chủ Linux 64 bit mới, có ít nhất 4 nhân CPU và 8 GB RAM.

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Mở fortserver trong trình duyệt tại `http://your-fortserver-ip/`

- Tên đăng nhập: `admin`
- Mật khẩu: `ChangeMe`

## Ảnh chụp màn hình

<p align="center">
  <img src="assets/screenshot-01.png" alt="Bảng điều khiển PAM của fortserver" width="49%" />
  <img src="assets/screenshot-02.png" alt="Quản lý tài sản trong fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-03.png" alt="Hộp thoại kết nối SSH của fortserver" width="49%" />
  <img src="assets/screenshot-04.png" alt="Yêu cầu AI từ terminal fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-05.png" alt="Trợ lý AI của fortserver" width="49%" />
  <img src="assets/screenshot-06.png" alt="Phiên máy tính từ xa trong fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-07.png" alt="Bảng tài sản terminal fortserver ở giao diện sáng" width="49%" />
  <img src="assets/screenshot-08.png" alt="Phiên SSH fortserver ở giao diện sáng" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-09.png" alt="Bảng tài sản terminal fortserver ở giao diện tối" width="49%" />
  <img src="assets/screenshot-10.png" alt="Phiên SSH fortserver ở giao diện tối" width="49%" />
</p>

## Thành phần

Các thành phần của fortserver được nhóm theo vai trò. Các dự án cốt lõi cung cấp nền tảng, giao diện web, terminal, kết nối giao thức và khả năng AI. Các thành phần dành cho doanh nghiệp mở rộng quyền truy cập vào ứng dụng và giao thức. Các dịch vụ hỗ trợ xử lý bản ghi phiên làm việc và vận hành máy chủ, còn các công cụ triển khai giúp đơn giản hóa việc cài đặt và phân phối nội dung web.

### Dự án cốt lõi

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Dự án</th>
      <th width="135" align="center"><div align="center">Phiên bản</div></th>
      <th width="550" align="center"><div align="center">Mô tả</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/fortserver">fortserver</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/fortserver/tags"><img src="https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản fortserver" /></a></div></td>
      <td width="550" align="left">Nền tảng quản lý truy cập đặc quyền mã nguồn mở</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/lina">Lina</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/lina/tags"><img src="https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Lina" /></a></div></td>
      <td width="550" align="left">Giao diện web của fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/luna">Luna</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/luna/tags"><img src="https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Luna" /></a></div></td>
      <td width="550" align="left">Terminal web và ứng dụng khách gốc của fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/koko">KoKo</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/koko/tags"><img src="https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản KoKo" /></a></div></td>
      <td width="550" align="left">Bộ kết nối và proxy giao thức đa dụng của fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/chen">Chen</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/chen/tags"><img src="https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Chen" /></a></div></td>
      <td width="550" align="left">Bộ kết nối cơ sở dữ liệu trên web của fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/kael">Kael</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/kael/tags"><img src="https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Kael" /></a></div></td>
      <td width="550" align="left">Thành phần AI của fortserver</td>
    </tr>
  </tbody>
</table>

### Thành phần doanh nghiệp

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Dự án</th>
      <th width="135" align="center"><div align="center">Phiên bản</div></th>
      <th width="550" align="center"><div align="center">Mô tả</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/tinker">Tinker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Bộ kết nối ứng dụng Windows của fortserver (miễn phí cho phiên bản Cộng đồng)</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/Panda">Panda</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Bộ kết nối ứng dụng Linux của fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/razor">Razor</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Proxy giao thức RDP của fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/magnus">Magnus</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Proxy giao thức cơ sở dữ liệu của fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/nec">Nec</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Proxy giao thức VNC của fortserver Enterprise Edition</td>
    </tr>
  </tbody>
</table>

### Dịch vụ hỗ trợ

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Dự án</th>
      <th width="135" align="center"><div align="center">Phiên bản</div></th>
      <th width="550" align="center"><div align="center">Mô tả</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/video-worker">Video&nbsp;Worker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Dịch vụ chuyển mã bản ghi phiên làm việc của fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/jdmc">JDMC</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Phiên bản riêng tư" /></div></td>
      <td width="550" align="left">Dịch vụ vận hành và quản lý máy chủ của fortserver Enterprise Edition</td>
    </tr>
  </tbody>
</table>

### Triển khai và công cụ

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Dự án</th>
      <th width="135" align="center"><div align="center">Phiên bản</div></th>
      <th width="550" align="center"><div align="center">Mô tả</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/installer">Installer</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/installer/tags"><img src="https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Installer" /></a></div></td>
      <td width="550" align="left">Công cụ cài đặt và quản lý fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/docker-web">Docker&nbsp;Web</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/docker-web/tags"><img src="https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Phiên bản Docker Web" /></a></div></td>
      <td width="550" align="left">Cổng web và tài nguyên tĩnh của fortserver</td>
    </tr>
  </tbody>
</table>

## Đóng góp

Chúng tôi hoan nghênh mọi đóng góp. Xem [CONTRIBUTING.md][contributing-link] để biết hướng dẫn.

## Giấy phép

Bản quyền (c) 2014-2026 fortserver. Bảo lưu mọi quyền.

Dự án được cấp phép theo Giấy phép Công cộng GNU phiên bản 3 (GPLv3, sau đây gọi là "Giấy phép"); bạn chỉ được sử dụng tệp này khi tuân thủ Giấy phép. Bạn có thể xem bản sao của Giấy phép tại

https://www.gnu.org/licenses/gpl-3.0.html

Trừ khi pháp luật hiện hành yêu cầu hoặc có thỏa thuận bằng văn bản, phần mềm được phân phối theo Giấy phép được cung cấp "NGUYÊN TRẠNG", KHÔNG KÈM BẤT KỲ BẢO ĐẢM HAY ĐIỀU KIỆN NÀO, dù rõ ràng hay ngụ ý. Xem Giấy phép để biết các quy định cụ thể về quyền và giới hạn.

<!-- fortserver official link -->
[docs-link]: https://fortserver.com/docs
[discord-link]: https://discord.com/invite/W6vYXmAQG2
[deepwiki-link]: https://deepwiki.com/fortserver/fortserver/
[contributing-link]: https://github.com/fortserver/fortserver/blob/dev/CONTRIBUTING.md

<!-- fortserver Other link-->
[license-link]: https://www.gnu.org/licenses/gpl-3.0.html
[docker-link]: https://hub.docker.com/u/fortserver
[github-release-link]: https://github.com/fortserver/fortserver/releases/latest
[github-stars-link]: https://github.com/fortserver/fortserver
[github-issues-link]: https://github.com/fortserver/fortserver/issues

<!-- Shield link-->
[docs-shield]: https://img.shields.io/badge/documentation-148F76
[github-release-shield]: https://img.shields.io/github/v/release/fortserver/fortserver
[github-stars-shield]: https://img.shields.io/github/stars/fortserver/fortserver?color=%231890FF&style=flat-square   
[docker-shield]: https://img.shields.io/docker/pulls/fortserver/jms_all.svg
[license-shield]: https://img.shields.io/github/license/fortserver/fortserver
[deepwiki-shield]: https://img.shields.io/badge/deepwiki-devin?color=blue
[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb
