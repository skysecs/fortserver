<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## オープンソースのPAMツール (バスティオンホスト)

</div>
<br/>

## fortserverとは？

fortserverは、DevOpsおよびITチームに対して、SSH、RDP、Kubernetes、データベース、リモートアプリケーションエンドポイントへのオンデマンドかつ安全なアクセスをウェブブラウザを通じて提供するオープンソースの特権アクセス管理 (PAM) ツールです。


<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/28676212-2bc4-4a9f-ae10-3be9320647e3">
  <img src="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f" alt="テーマに基づく画像">
</picture>


## クイックスタート

クリーンなLinuxサーバーを準備します (64ビット, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

ブラウザでfortserverにアクセスします `http://your-fortserver-ip/`
- ユーザー名: `admin`
- パスワード: `ChangeMe`

[![fortserver クイックスタート](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "fortserver クイックスタート")

## スクリーンショット
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="fortserver コンソール"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/7c1f81af-37e8-4f07-8ac9-182895e1062e" alt="fortserver PAM"   /></td>    
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="fortserver 監査"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="fortserver 作業台"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/eaa41f66-8cc8-4f01-a001-0d258501f1c9" alt="fortserver RBAC"   /></td>     
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

fortserverは複数の主要コンポーネントで構成されており、全体としてfortserverの機能フレームワークを形成し、ユーザーに対して運用管理およびセキュリティ制御の包括的な機能を提供します。

| プロジェクト                                            | ステータス                                                                                                                                                                 | 説明                                                                                                      |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/fortserver/lina)             | <a href="https://github.com/fortserver/lina/releases"><img alt="Linaのリリース" src="https://img.shields.io/github/release/fortserver/lina.svg" /></a>                   | fortserverウェブUI                                                                                       |
| [Luna](https://github.com/fortserver/luna)             | <a href="https://github.com/fortserver/luna/releases"><img alt="Lunaのリリース" src="https://img.shields.io/github/release/fortserver/luna.svg" /></a>                   | fortserverウェブ端末                                                                                     |
| [KoKo](https://github.com/fortserver/koko)             | <a href="https://github.com/fortserver/koko/releases"><img alt="Kokoのリリース" src="https://img.shields.io/github/release/fortserver/koko.svg" /></a>                   | fortserverキャラクタプロトコルコネクタ                                                                   |
| [Lion](https://github.com/fortserver/lion)             | <a href="https://github.com/fortserver/lion/releases"><img alt="Lionのリリース" src="https://img.shields.io/github/release/fortserver/lion.svg" /></a>                   | fortserverグラフィカルプロトコルコネクタ                                                                  |
| [Chen](https://github.com/fortserver/chen)             | <a href="https://github.com/fortserver/chen/releases"><img alt="Chenのリリース" src="https://img.shields.io/github/release/fortserver/chen.svg" />                       | fortserverウェブデータベース                                                                                |  
| [Tinker](https://github.com/fortserver/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | fortserverリモートアプリケーションコネクタ (Windows)                                                |
| [Panda](https://github.com/fortserver/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | fortserver EEリモートアプリケーションコネクタ (Linux)                                                   |
| [Razor](https://github.com/fortserver/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | fortserver EE RDPプロキシコネクタ                                                                         |
| [Magnus](https://github.com/fortserver/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                             | fortserver EEデータベースプロキシコネクタ                                                                  |
| [Nec](https://github.com/fortserver/nec)               | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | fortserver EE VNCプロキシコネクタ                                                                         |
| [Facelive](https://github.com/fortserver/facelive)     | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | fortserver EE顔認識                                                                                       |


## 貢献

貢献するためにPRを提出することを歓迎します。ガイドラインについては[CONTRIBUTING.md][contributing-link]を参照してください。

## ライセンス

Copyright (c) 2014-2025 fortserver, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

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