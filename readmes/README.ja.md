<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## オープンソースの PAM プラットフォーム (バスティオン ホスト)

</div>
<br/>

## fortserver とは？

fortserver は、AI 機能を備えたオープンソースの特権アクセス管理 (PAM) プラットフォームです。DevOps および IT チームに統一されたワークスペースを提供し、SSH、RDP、Kubernetes、データベース、Web サイト、RemoteApp、VirtualApp などへの安全なアクセスを実現します。

<img alt="fortserver アーキテクチャ図" src="https://github.com/user-attachments/assets/2bbf0979-4e1e-43ea-8dac-5d3e3bfbf1d1" />

## クイックスタート

クリーンな Linux サーバーを準備します (64 ビット, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

ブラウザで fortserver にアクセスします: `http://your-fortserver-ip/`
- ユーザー名: `admin`
- パスワード: `ChangeMe`


## スクリーンショット
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6164c92a-0b19-405a-b79c-73e28a9a1610" alt="fortserver Console"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/12d1206d-b511-4f29-8b00-fd13333f3a21" alt="fortserver PAM"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6d12d3c9-5f31-4294-b6e7-7c5b5836f688" alt="fortserver Audits"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ba784bc8-e889-4fd6-aaae-0b8b14153da2" alt="fortserver Workbench"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/d4b10b15-bccb-4a0d-a6e6-74a6439614e0" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ccbeb96e-9747-4182-bd03-031fb3af8bb2" alt="fortserver Settings"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/9049888e-16fe-4fbe-b0f2-16bf140379c8" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/133c4af6-90a9-457d-b372-bb53c29260dc" alt="fortserver Settings"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ea48738f-b5f8-4a43-a487-ca09b11176e7" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/3407539f-1235-4dcc-adf2-26d7b60dbc67" alt="fortserver Settings"   /></td>
  </tr>
</table>

## コンポーネント

fortserver は、複数の主要コンポーネントで構成されており、これらが集まって fortserver の機能的なフレームワークを形成し、ユーザーに対して運用管理およびセキュリティ制御の包括的な機能を提供します。

## プロジェクト

### コアプロジェクト

| プロジェクト | バージョン | 説明 |
| --- | --- | --- |
| [fortserver](https://github.com/fortserver/fortserver) | [![tag](https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/fortserver/tags) | オープンソースの特権アクセス管理プラットフォーム |
| [Lina](https://github.com/fortserver/lina) | [![tag](https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/lina/tags) | fortserver Web UI |
| [Luna](https://github.com/fortserver/luna) | [![tag](https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/luna/tags) | fortserver Web ターミナルおよびネイティブクライアント |
| [KoKo](https://github.com/fortserver/koko) | [![tag](https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/koko/tags) | fortserver 汎用プロトコルコネクターおよびプロキシ |
| [Chen](https://github.com/fortserver/chen) | [![tag](https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/chen/tags) | fortserver Web データベースコネクター |
| [Kael](https://github.com/fortserver/kael) | [![tag](https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/kael/tags) | fortserver AI コンポーネント |

### エンタープライズ版コンポーネント

| プロジェクト | バージョン | 説明 |
| --- | --- | --- |
| [Tinker](https://github.com/fortserver/tinker) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver Windows アプリケーションコネクター（コミュニティ版で無料利用可能） |
| [Panda](https://github.com/fortserver/Panda) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版 Linux アプリケーションコネクター |
| [Razor](https://github.com/fortserver/razor) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版 RDP プロトコルプロキシ |
| [Magnus](https://github.com/fortserver/magnus) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版データベースプロトコルプロキシ |
| [Nec](https://github.com/fortserver/nec) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版 VNC プロトコルプロキシ |

### サポートサービス

| プロジェクト | バージョン | 説明 |
| --- | --- | --- |
| [Video Worker](https://github.com/fortserver/video-worker) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版セッション録画トランスコードワーカー |
| [JDMC](https://github.com/fortserver/jdmc) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver エンタープライズ版ホスト運用管理サービス |

### デプロイとツール

| プロジェクト | バージョン | 説明 |
| --- | --- | --- |
| [Installer](https://github.com/fortserver/installer) | [![tag](https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/installer/tags) | fortserver インストールおよび管理ツール |
| [Docker Web](https://github.com/fortserver/docker-web) | [![tag](https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/docker-web/tags) | fortserver Web ゲートウェイおよび静的アセット |

## 貢献

PR を提出して貢献していただけると幸いです。ガイドラインについては [CONTRIBUTING.md][contributing-link] を参照してください。

## ライセンス

Copyright (c) 2014-2025 fortserver, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

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