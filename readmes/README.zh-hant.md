<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## 開源特權存取管理（PAM）平台（堡壘機）

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

## 什麼是 fortserver？

fortserver 是具備 AI 能力的開源特權存取管理（PAM）平台，為 DevOps 和 IT 團隊提供統一的工作空間，安全存取 SSH、RDP、Kubernetes、資料庫、網站、RemoteApp、VirtualApp 等資源。

<img alt="fortserver 架構圖" src="assets/fortserver-architecture.png" />

## 快速開始

準備一台乾淨的 64 位元 Linux 伺服器，至少配備 4 核心 CPU 和 8 GB 記憶體。

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

在瀏覽器中開啟 fortserver： `http://your-fortserver-ip/`

- 使用者名稱: `admin`
- 密碼: `ChangeMe`

## 畫面截圖

<p align="center">
  <img src="assets/screenshot-01.png" alt="fortserver 特權存取管理儀表板" width="49%" />
  <img src="assets/screenshot-02.png" alt="fortserver 資產管理" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-03.png" alt="fortserver SSH 連線對話方塊" width="49%" />
  <img src="assets/screenshot-04.png" alt="fortserver 終端機 AI 提問" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-05.png" alt="fortserver AI 助理" width="49%" />
  <img src="assets/screenshot-06.png" alt="fortserver 遠端桌面工作階段" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-07.png" alt="fortserver 淺色主題終端機資產面板" width="49%" />
  <img src="assets/screenshot-08.png" alt="fortserver 淺色主題 SSH 工作階段" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-09.png" alt="fortserver 深色主題終端機資產面板" width="49%" />
  <img src="assets/screenshot-10.png" alt="fortserver 深色主題 SSH 工作階段" width="49%" />
</p>

## 元件

fortserver 依職責劃分元件。核心專案提供平台、Web 介面、終端機、協定連線及 AI 能力；企業版元件擴充應用程式與協定存取；支援服務處理工作階段錄影及主機維運；部署工具簡化安裝與 Web 資源交付。

### 核心專案

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">專案</th>
      <th width="135" align="center"><div align="center">版本</div></th>
      <th width="550" align="center"><div align="center">說明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/fortserver">fortserver</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/fortserver/tags"><img src="https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&amp;filter=v5.*&amp;label=tag" alt="fortserver 版本" /></a></div></td>
      <td width="550" align="left">開源特權存取管理平台</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/lina">Lina</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/lina/tags"><img src="https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Lina 版本" /></a></div></td>
      <td width="550" align="left">fortserver Web 介面</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/luna">Luna</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/luna/tags"><img src="https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Luna 版本" /></a></div></td>
      <td width="550" align="left">fortserver Web 終端機與原生用戶端</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/koko">KoKo</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/koko/tags"><img src="https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&amp;filter=v5.*&amp;label=tag" alt="KoKo 版本" /></a></div></td>
      <td width="550" align="left">fortserver 通用協定連接器與代理</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/chen">Chen</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/chen/tags"><img src="https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Chen 版本" /></a></div></td>
      <td width="550" align="left">fortserver Web 資料庫連接器</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/kael">Kael</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/kael/tags"><img src="https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Kael 版本" /></a></div></td>
      <td width="550" align="left">fortserver AI 元件</td>
    </tr>
  </tbody>
</table>

### 企業版元件

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">專案</th>
      <th width="135" align="center"><div align="center">版本</div></th>
      <th width="550" align="center"><div align="center">說明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/tinker">Tinker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver Windows 應用程式連接器（社群版可免費使用）</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/Panda">Panda</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版 Linux 應用程式連接器</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/razor">Razor</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版 RDP 協定代理</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/magnus">Magnus</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版資料庫協定代理</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/nec">Nec</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版 VNC 協定代理</td>
    </tr>
  </tbody>
</table>

### 支援服務

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">專案</th>
      <th width="135" align="center"><div align="center">版本</div></th>
      <th width="550" align="center"><div align="center">說明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/video-worker">Video&nbsp;Worker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版工作階段錄影轉碼服務</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/jdmc">JDMC</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="私有版本" /></div></td>
      <td width="550" align="left">fortserver 企業版主機維運與管理服務</td>
    </tr>
  </tbody>
</table>

### 部署與工具

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">專案</th>
      <th width="135" align="center"><div align="center">版本</div></th>
      <th width="550" align="center"><div align="center">說明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/installer">Installer</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/installer/tags"><img src="https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Installer 版本" /></a></div></td>
      <td width="550" align="left">fortserver 安裝與管理工具</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/docker-web">Docker&nbsp;Web</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/docker-web/tags"><img src="https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Docker Web 版本" /></a></div></td>
      <td width="550" align="left">fortserver Web 閘道與靜態資源</td>
    </tr>
  </tbody>
</table>

## 參與貢獻

歡迎提交貢獻。請參閱 [CONTRIBUTING.md][contributing-link] 了解貢獻指南。

## 授權條款

著作權所有 (c) 2014-2026 fortserver。保留所有權利。

本專案依 GNU 通用公眾授權條款第 3 版（GPLv3，以下稱「授權條款」）授權；您只能在遵守授權條款的前提下使用本檔案。授權條款副本可於以下網址取得：

https://www.gnu.org/licenses/gpl-3.0.html

除非適用法律要求或另有書面約定，依授權條款散布的軟體均以「現狀」提供，不附帶任何明示或默示的保證或條件。相關權限與限制請參閱授權條款中的具體規定。

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
