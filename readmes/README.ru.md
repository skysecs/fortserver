<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Открытая платформа PAM (хост-бастион)

</div>
<br/>

## Что такое fortserver?

fortserver — это платформа управления привилегированным доступом (PAM) с открытым исходным кодом и возможностями ИИ, предоставляющая командам DevOps и ИТ единое рабочее пространство для безопасного доступа к SSH, RDP, Kubernetes, базам данных, веб-сайтам, RemoteApp, VirtualApp и другим ресурсам.

<img alt="Схема архитектуры fortserver" src="https://github.com/user-attachments/assets/2bbf0979-4e1e-43ea-8dac-5d3e3bfbf1d1" />

## Быстрый старт

Подготовьте чистый сервер Linux (64 бит, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Доступ к fortserver в вашем браузере по адресу `http://your-fortserver-ip/`
- Имя пользователя: `admin`
- Пароль: `ChangeMe`


## Скриншоты
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

## Компоненты

fortserver состоит из нескольких ключевых компонентов, которые вместе образуют функциональную основу fortserver, предоставляя пользователям комплексные возможности для управления операциями и контроля безопасности.

## Проекты

### Основные проекты

| Проект | Версия | Описание |
| --- | --- | --- |
| [fortserver](https://github.com/fortserver/fortserver) | [![tag](https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/fortserver/tags) | Платформа управления привилегированным доступом с открытым исходным кодом |
| [Lina](https://github.com/fortserver/lina) | [![tag](https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/lina/tags) | Веб-интерфейс fortserver |
| [Luna](https://github.com/fortserver/luna) | [![tag](https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/luna/tags) | Веб-терминал и нативный клиент fortserver |
| [KoKo](https://github.com/fortserver/koko) | [![tag](https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/koko/tags) | Универсальный коннектор и прокси протоколов fortserver |
| [Chen](https://github.com/fortserver/chen) | [![tag](https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/chen/tags) | Веб-коннектор баз данных fortserver |
| [Kael](https://github.com/fortserver/kael) | [![tag](https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/kael/tags) | Компонент ИИ fortserver |

### Компоненты корпоративной редакции

| Проект | Версия | Описание |
| --- | --- | --- |
| [Tinker](https://github.com/fortserver/tinker) | ![tag](https://img.shields.io/badge/tag-private-red) | Коннектор приложений Windows для fortserver (бесплатно для редакции Community) |
| [Panda](https://github.com/fortserver/Panda) | ![tag](https://img.shields.io/badge/tag-private-red) | Коннектор приложений Linux корпоративной редакции fortserver |
| [Razor](https://github.com/fortserver/razor) | ![tag](https://img.shields.io/badge/tag-private-red) | Прокси протокола RDP корпоративной редакции fortserver |
| [Magnus](https://github.com/fortserver/magnus) | ![tag](https://img.shields.io/badge/tag-private-red) | Прокси протоколов баз данных корпоративной редакции fortserver |
| [Nec](https://github.com/fortserver/nec) | ![tag](https://img.shields.io/badge/tag-private-red) | Прокси протокола VNC корпоративной редакции fortserver |

### Вспомогательные сервисы

| Проект | Версия | Описание |
| --- | --- | --- |
| [Video Worker](https://github.com/fortserver/video-worker) | ![tag](https://img.shields.io/badge/tag-private-red) | Сервис перекодирования записей сеансов корпоративной редакции fortserver |
| [JDMC](https://github.com/fortserver/jdmc) | ![tag](https://img.shields.io/badge/tag-private-red) | Сервис эксплуатации и управления хостами корпоративной редакции fortserver |

### Развёртывание и инструменты

| Проект | Версия | Описание |
| --- | --- | --- |
| [Installer](https://github.com/fortserver/installer) | [![tag](https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/installer/tags) | Инструмент установки и управления fortserver |
| [Docker Web](https://github.com/fortserver/docker-web) | [![tag](https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&filter=v5.*&label=tag)](https://github.com/fortserver/docker-web/tags) | Веб-шлюз и статические ресурсы fortserver |

## Участие

Добро пожаловать, чтобы подать PR для участия. Пожалуйста, обратитесь к [CONTRIBUTING.md][contributing-link] за руководством.

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