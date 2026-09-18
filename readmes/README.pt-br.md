<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Uma plataforma de PAM de código aberto (Bastion Host)

</div>
<br/>

## O que é fortserver?

fortserver é uma plataforma de gerenciamento de acesso privilegiado (PAM) de código aberto com recursos de IA que oferece às equipes de DevOps e TI um espaço de trabalho unificado para acessar com segurança SSH, RDP, Kubernetes, bancos de dados, sites, RemoteApp, VirtualApp e muito mais.

<img alt="Diagrama de arquitetura do fortserver" src="https://github.com/user-attachments/assets/2bbf0979-4e1e-43ea-8dac-5d3e3bfbf1d1" />

## Início rápido

Prepare um Servidor Linux limpo ( 64 bits, >= 4c8g )

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Acesse o fortserver em seu navegador em `http://your-fortserver-ip/`
- Nome de usuário: `admin`
- Senha: `ChangeMe`


## Capturas de tela
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6164c92a-0b19-405a-b79c-73e28a9a1610" alt="Console do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/12d1206d-b511-4f29-8b00-fd13333f3a21" alt="fortserver PAM"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/6d12d3c9-5f31-4294-b6e7-7c5b5836f688" alt="Auditorias do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ba784bc8-e889-4fd6-aaae-0b8b14153da2" alt="Banco de Trabalho do fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/d4b10b15-bccb-4a0d-a6e6-74a6439614e0" alt="RBAC do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ccbeb96e-9747-4182-bd03-031fb3af8bb2" alt="Configurações do fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/9049888e-16fe-4fbe-b0f2-16bf140379c8" alt="RBAC do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/133c4af6-90a9-457d-b372-bb53c29260dc" alt="Configurações do fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/ea48738f-b5f8-4a43-a487-ca09b11176e7" alt="RBAC do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/3407539f-1235-4dcc-adf2-26d7b60dbc67" alt="Configurações do fortserver"   /></td>
  </tr>
</table>

## Componentes

fortserver consiste em múltiplos componentes principais, que coletivamente formam a estrutura funcional do fortserver, proporcionando aos usuários capacidades abrangentes para gerenciamento de operações e controle de segurança.

## Projetos

### Projetos principais

| Projeto | Versão | Descrição |
| --- | --- | --- |
| [fortserver](https://github.com/fortserver/fortserver) | [![tag](https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/fortserver/tags) | Plataforma de gerenciamento de acesso privilegiado de código aberto |
| [Lina](https://github.com/fortserver/lina) | [![tag](https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/lina/tags) | Interface web do fortserver |
| [Luna](https://github.com/fortserver/luna) | [![tag](https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/luna/tags) | Terminal web e cliente nativo do fortserver |
| [KoKo](https://github.com/fortserver/koko) | [![tag](https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/koko/tags) | Conector e proxy de protocolos de uso geral do fortserver |
| [Chen](https://github.com/fortserver/chen) | [![tag](https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/chen/tags) | Conector web de bancos de dados do fortserver |
| [Kael](https://github.com/fortserver/kael) | [![tag](https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/kael/tags) | Componente de IA do fortserver |

### Componentes empresariais

| Projeto | Versão | Descrição |
| --- | --- | --- |
| [Tinker](https://github.com/fortserver/tinker) | ![tag](https://img.shields.io/badge/tag-private-red) | Conector de aplicativos Windows do fortserver (gratuito para a edição comunitária) |
| [Panda](https://github.com/fortserver/Panda) | ![tag](https://img.shields.io/badge/tag-private-red) | Conector de aplicativos Linux da edição empresarial do fortserver |
| [Razor](https://github.com/fortserver/razor) | ![tag](https://img.shields.io/badge/tag-private-red) | Proxy do protocolo RDP da edição empresarial do fortserver |
| [Magnus](https://github.com/fortserver/magnus) | ![tag](https://img.shields.io/badge/tag-private-red) | Proxy de protocolos de bancos de dados da edição empresarial do fortserver |
| [Nec](https://github.com/fortserver/nec) | ![tag](https://img.shields.io/badge/tag-private-red) | Proxy do protocolo VNC da edição empresarial do fortserver |

### Serviços de apoio

| Projeto | Versão | Descrição |
| --- | --- | --- |
| [Video Worker](https://github.com/fortserver/video-worker) | ![tag](https://img.shields.io/badge/tag-private-red) | Serviço de transcodificação de gravações de sessões da edição empresarial do fortserver |
| [JDMC](https://github.com/fortserver/jdmc) | ![tag](https://img.shields.io/badge/tag-private-red) | Serviço de operações e gerenciamento de hosts da edição empresarial do fortserver |

### Implantação e ferramentas

| Projeto | Versão | Descrição |
| --- | --- | --- |
| [Installer](https://github.com/fortserver/installer) | [![tag](https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/installer/tags) | Ferramenta de instalação e gerenciamento do fortserver |
| [Docker Web](https://github.com/fortserver/docker-web) | [![tag](https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/docker-web/tags) | Gateway web e recursos estáticos do fortserver |

## Contribuindo

Bem-vindo para enviar PR para contribuir. Consulte [CONTRIBUTING.md][contributing-link] para diretrizes.

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