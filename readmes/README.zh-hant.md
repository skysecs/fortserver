<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## 一個開源的 PAM 平台 (堡壘主機)

</div>
<br/>

## fortserver 是什麼？

fortserver 是一個具備 AI 能力的開源特權訪問管理 (PAM) 平台，為 DevOps 和 IT 團隊提供統一的工作空間，以安全訪問 SSH、RDP、Kubernetes、數據庫、網站、RemoteApp、VirtualApp 等資源。

<img alt="fortserver 架構圖" src="https://github.com/user-attachments/assets/2bbf0979-4e1e-43ea-8dac-5d3e3bfbf1d1" />

## 快速開始

準備一台乾淨的 Linux 伺服器 (64 位，>= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

在您的瀏覽器中訪問 fortserver，地址為 `http://your-fortserver-ip/`
- 用戶名：`admin`
- 密碼：`ChangeMe`


## 畫面截圖
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6164c92a-0b19-405a-b79c-73e28a9a1610" alt="fortserver 控制台"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/12d1206d-b511-4f29-8b00-fd13333f3a21" alt="fortserver PAM"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6d12d3c9-5f31-4294-b6e7-7c5b5836f688" alt="fortserver 審計"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ba784bc8-e889-4fd6-aaae-0b8b14153da2" alt="fortserver 工作台"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/d4b10b15-bccb-4a0d-a6e6-74a6439614e0" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ccbeb96e-9747-4182-bd03-031fb3af8bb2" alt="fortserver 設定"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/9049888e-16fe-4fbe-b0f2-16bf140379c8" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/133c4af6-90a9-457d-b372-bb53c29260dc" alt="fortserver 設定"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ea48738f-b5f8-4a43-a487-ca09b11176e7" alt="fortserver RBAC"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/3407539f-1235-4dcc-adf2-26d7b60dbc67" alt="fortserver 設定"   /></td>
  </tr>
</table>

## 組件

fortserver 由多個關鍵組件組成，這些組件共同構成了 fortserver 的功能框架，為用戶提供全面的操作管理和安全控制能力。

## 項目

### 核心項目

| 項目 | 版本 | 描述 |
| --- | --- | --- |
| [fortserver](https://github.com/fortserver/fortserver) | [![tag](https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/fortserver/tags) | 開源特權訪問管理平台 |
| [Lina](https://github.com/fortserver/lina) | [![tag](https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/lina/tags) | fortserver 網頁 UI |
| [Luna](https://github.com/fortserver/luna) | [![tag](https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/luna/tags) | fortserver 網頁終端和原生客戶端 |
| [KoKo](https://github.com/fortserver/koko) | [![tag](https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/koko/tags) | fortserver 通用協議連接器和代理 |
| [Chen](https://github.com/fortserver/chen) | [![tag](https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/chen/tags) | fortserver 網頁數據庫連接器 |
| [Kael](https://github.com/fortserver/kael) | [![tag](https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/kael/tags) | fortserver AI 組件 |

### 企業版組件

| 項目 | 版本 | 描述 |
| --- | --- | --- |
| [Tinker](https://github.com/fortserver/tinker) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver Windows 應用連接器（社群版免費使用） |
| [Panda](https://github.com/fortserver/Panda) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版 Linux 應用連接器 |
| [Razor](https://github.com/fortserver/razor) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版 RDP 協議代理 |
| [Magnus](https://github.com/fortserver/magnus) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版數據庫協議代理 |
| [Nec](https://github.com/fortserver/nec) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版 VNC 協議代理 |

### 配套服務

| 項目 | 版本 | 描述 |
| --- | --- | --- |
| [Video Worker](https://github.com/fortserver/video-worker) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版會話錄影轉碼服務 |
| [JDMC](https://github.com/fortserver/jdmc) | ![tag](https://img.shields.io/badge/tag-private-red) | fortserver 企業版主機維運管理服務 |

### 部署與工具

| 項目 | 版本 | 描述 |
| --- | --- | --- |
| [Installer](https://github.com/fortserver/installer) | [![tag](https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/installer/tags) | fortserver 安裝和管理工具 |
| [Docker Web](https://github.com/fortserver/docker-web) | [![tag](https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/docker-web/tags) | fortserver Web 閘道和靜態資源 |

## 貢獻

歡迎提交 PR 以貢獻。請參考 [CONTRIBUTING.md][contributing-link] 獲取指南。

## License

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