<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.org/index-en.html"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## An open-source PAM tool (Bastion Host)

[![][license-shield]][license-link]
[![][discord-shield]][discord-link]
[![][docker-shield]][docker-link]
[![][github-release-shield]][github-release-link]
[![][github-stars-shield]][github-stars-link]

[English](/README.md) · [中文(简体)](/readmes/README.zh-hans.md) · [中文(繁體)](/readmes/README.zh-hant.md) · [日本語](/readmes/README.ja.md) · [Português (Brasil)](/readmes/README.pt-br.md)

</div>
<br/>

## fortserverとは？

fortserverは、DevOpsおよびITチームに対して、ウェブブラウザを通じてSSH、RDP、Kubernetes、データベース、RemoteAppエンドポイントに対するオンデマンドかつ安全なアクセスを提供する、オープンソースの特権アクセス管理（PAM）ツールです。

![fortserver 概要](https://github.com/fortserver/fortserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## クイックスタート

クリーンなLinuxサーバーを準備してください (64ビット, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

ブラウザでfortserverにアクセスする: `http://your-fortserver-ip/`
- ユーザー名: `admin`
- パスワード: `ChangeMe`

[![fortserver クイックスタート](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "fortserver クイックスタート")

## スクリーンショット

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="fortserver コンソール"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="fortserver 監査"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="fortserver ワークベンチ"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="fortserver 設定"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="fortserver SSH"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="fortserver RDP"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="fortserver K8s"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="fortserver DB"   /></td>
  </tr>
</table>

## コンポーネント

fortserverは複数の主要コンポーネントで構成されており、これらが集まってfortserverの機能的なフレームワークを形成し、操作管理とセキュリティ制御のための包括的な機能をユーザーに提供します。

| プロジェクト                                               | ステータス                                                                                                                                                                  | 説明                                                                                                 |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/fortserver/lina)             | <a href="https://github.com/fortserver/lina/releases"><img alt="Lina リリース" src="https://img.shields.io/github/release/fortserver/lina.svg" /></a>                   | fortserver ウェブUI                                                                                   |
| [Luna](https://github.com/fortserver/luna)             | <a href="https://github.com/fortserver/luna/releases"><img alt="Luna リリース" src="https://img.shields.io/github/release/fortserver/luna.svg" /></a>                   | fortserver ウェブターミナル                                                                             |
| [KoKo](https://github.com/fortserver/koko)             | <a href="https://github.com/fortserver/koko/releases"><img alt="Koko リリース" src="https://img.shields.io/github/release/fortserver/koko.svg" /></a>                   | fortserver キャラクタプロトコルコネクタ                                                                  |
| [Lion](https://github.com/fortserver/lion)             | <a href="https://github.com/fortserver/lion/releases"><img alt="Lion リリース" src="https://img.shields.io/github/release/fortserver/lion.svg" /></a>                   | fortserver グラフィカルプロトコルコネクタ                                                            |
| [Chen](https://github.com/fortserver/chen)             | <a href="https://github.com/fortserver/chen/releases"><img alt="Chen リリース" src="https://img.shields.io/github/release/fortserver/chen.svg" />                       | fortserver ウェブDB                                                                                   |  
| [Razor](https://github.com/fortserver/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | fortserver EE RDPプロキシコネクタ                                                                       |
| [Tinker](https://github.com/fortserver/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | fortserver EE リモートアプリケーションコネクタ (Windows)                                              |
| [Panda](https://github.com/fortserver/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | fortserver EE リモートアプリケーションコネクタ (Linux)                                               |
| [Magnus](https://github.com/fortserver/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | fortserver EE データベースプロキシコネクタ                                                             |
| [Nec](https://github.com/fortserver/nec)               | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | fortserver EE VNCプロキシコネクタ                                                                       |
| [Facelive](https://github.com/fortserver/facelive)     | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | fortserver EE 顔認識                                                                                  |


## 貢献

PRを提出して貢献することを歓迎します。ガイドラインについては[CONTRIBUTING.md][contributing-link]を参照してください。

## セキュリティ

fortserverはミッションクリティカルな製品です。インストールおよびデプロイメントのための基本的セキュリティ推奨事項を参照してください。セキュリティ関連の問題に遭遇した場合は、直接ご連絡ください:

- メール: support@fortserver.com

## License


<!-- fortserver official link -->
[docs-link]: https://fortserver.com/docs
[discord-link]: https://discord.com/invite/W6vYXmAQG2
[contributing-link]: https://github.com/fortserver/fortserver/blob/dev/CONTRIBUTING.md

<!-- fortserver Other link-->
[license-link]: https://www.gnu.org/licenses/gpl-3.0.html
[docker-link]: https://hub.docker.com/u/fortserver
[github-release-link]: https://github.com/fortserver/fortserver/releases/latest
[github-stars-link]: https://github.com/fortserver/fortserver
[github-issues-link]: https://github.com/fortserver/fortserver/issues

<!-- Shield link-->
[github-release-shield]: https://img.shields.io/github/v/release/fortserver/fortserver
[github-stars-shield]: https://img.shields.io/github/stars/fortserver/fortserver?color=%231890FF&style=flat-square
[docker-shield]: https://img.shields.io/docker/pulls/fortserver/jms_all.svg
[license-shield]: https://img.shields.io/github/license/fortserver/fortserver
[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb

<!-- Image link -->
