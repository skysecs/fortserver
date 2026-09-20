<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## An open-source PAM platform (Bastion Host)

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

## What is fortserver?

fortserver is an open-source Privileged Access Management (PAM) platform with AI-powered capabilities. It gives DevOps and IT teams a unified workspace for secure access to SSH, RDP, Kubernetes, databases, websites, RemoteApp, VirtualApp, and more.

<img alt="fortserver architecture diagram" src="assets/fortserver-architecture.png" />

## Quickstart

Prepare a clean 64-bit Linux server with at least 4 CPU cores and 8 GB of RAM.

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Open fortserver in your browser at `http://your-fortserver-ip/`

- Username: `admin`
- Password: `ChangeMe`

## Screenshots

<p align="center">
  <img src="assets/screenshot-01.png" alt="fortserver PAM dashboard" width="49%" />
  <img src="assets/screenshot-02.png" alt="fortserver asset management" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-03.png" alt="fortserver SSH connection dialog" width="49%" />
  <img src="assets/screenshot-04.png" alt="fortserver terminal AI prompt" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-05.png" alt="fortserver AI assistant" width="49%" />
  <img src="assets/screenshot-06.png" alt="fortserver remote desktop session" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-07.png" alt="fortserver terminal asset panel in light theme" width="49%" />
  <img src="assets/screenshot-08.png" alt="fortserver SSH session in light theme" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-09.png" alt="fortserver terminal asset panel in dark theme" width="49%" />
  <img src="assets/screenshot-10.png" alt="fortserver SSH session in dark theme" width="49%" />
</p>

## Components

fortserver groups its components by role. Core projects provide the platform, web interface, terminal, protocol connections, and AI capabilities. Enterprise components extend application and protocol access. Supporting services handle session recordings and host operations, while deployment tools simplify installation and web delivery.

### Core Projects

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Project</th>
      <th width="135" align="center"><div align="center">Version</div></th>
      <th width="550" align="center"><div align="center">Description</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/fortserver">fortserver</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/fortserver/tags"><img src="https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&amp;filter=v5.*&amp;label=tag" alt="fortserver version" /></a></div></td>
      <td width="550" align="left">Open-source Privileged Access Management platform</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/lina">Lina</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/lina/tags"><img src="https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Lina version" /></a></div></td>
      <td width="550" align="left">fortserver web interface</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/luna">Luna</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/luna/tags"><img src="https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Luna version" /></a></div></td>
      <td width="550" align="left">fortserver web terminal and native client</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/koko">KoKo</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/koko/tags"><img src="https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&amp;filter=v5.*&amp;label=tag" alt="KoKo version" /></a></div></td>
      <td width="550" align="left">fortserver general-purpose protocol connector and proxy</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/chen">Chen</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/chen/tags"><img src="https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Chen version" /></a></div></td>
      <td width="550" align="left">fortserver web database connector</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/kael">Kael</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/kael/tags"><img src="https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Kael version" /></a></div></td>
      <td width="550" align="left">fortserver AI component</td>
    </tr>
  </tbody>
</table>

### Enterprise Components

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Project</th>
      <th width="135" align="center"><div align="center">Version</div></th>
      <th width="550" align="center"><div align="center">Description</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/tinker">Tinker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Windows application connector (free for Community Edition)</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/Panda">Panda</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition Linux application connector</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/razor">Razor</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition RDP protocol proxy</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/magnus">Magnus</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition database protocol proxy</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/nec">Nec</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition VNC protocol proxy</td>
    </tr>
  </tbody>
</table>

### Supporting Services

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Project</th>
      <th width="135" align="center"><div align="center">Version</div></th>
      <th width="550" align="center"><div align="center">Description</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/video-worker">Video&nbsp;Worker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition session recording transcoding worker</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/jdmc">JDMC</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Private version" /></div></td>
      <td width="550" align="left">fortserver Enterprise Edition host operations and management service</td>
    </tr>
  </tbody>
</table>

### Deployment & Tooling

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Project</th>
      <th width="135" align="center"><div align="center">Version</div></th>
      <th width="550" align="center"><div align="center">Description</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/installer">Installer</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/installer/tags"><img src="https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Installer version" /></a></div></td>
      <td width="550" align="left">fortserver installation and management tool</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/docker-web">Docker&nbsp;Web</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/docker-web/tags"><img src="https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Docker Web version" /></a></div></td>
      <td width="550" align="left">fortserver web gateway and static assets</td>
    </tr>
  </tbody>
</table>

## Contributing

Contributions are welcome. See [CONTRIBUTING.md][contributing-link] for guidelines.

## License

Copyright (c) 2014-2026 fortserver, All rights reserved.

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
