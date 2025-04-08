<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Инструмент PAM с открытым исходным кодом (Bastion Host)

</div>
<br/>

## Что такое fortserver?

fortserver - это инструмент управления привилегированным доступом (PAM) с открытым исходным кодом, который предоставляет командам DevOps и ИТ безопасный доступ по запросу к конечным точкам SSH, RDP, Kubernetes, базам данных и RemoteApp через веб-браузер.


<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/28676212-2bc4-4a9f-ae10-3be9320647e3">
  <img src="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f" alt="Изображение на основе темы">
</picture>


## Быстрый старт

Подготовьте чистый сервер Linux (64 бит, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Получите доступ к fortserver в вашем браузере по адресу `http://your-fortserver-ip/`
- Имя пользователя: `admin`
- Пароль: `ChangeMe`

[![fortserver Quickstart](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "fortserver Quickstart")

## Скриншоты
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="Консоль fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/7c1f81af-37e8-4f07-8ac9-182895e1062e" alt="fortserver PAM"   /></td>    
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="Аудиты fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="Рабочая станция fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/eaa41f66-8cc8-4f01-a001-0d258501f1c9" alt="RBAC fortserver"   /></td>     
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="Настройки fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="SSH fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="RDP fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="K8s fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="DB fortserver"   /></td>
  </tr>
</table>

## Компоненты

fortserver состоит из нескольких ключевых компонентов, которые вместе формируют функциональную структуру fortserver, предоставляя пользователям широкие возможности для управления операциями и контроля безопасности.

| Проект                                                 | Статус                                                                                                                                                                 | Описание                                                                                             |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/fortserver/lina)             | <a href="https://github.com/fortserver/lina/releases"><img alt="Выпуск Lina" src="https://img.shields.io/github/release/fortserver/lina.svg" /></a>                   | Веб-интерфейс fortserver                                                                                |
| [Luna](https://github.com/fortserver/luna)             | <a href="https://github.com/fortserver/luna/releases"><img alt="Выпуск Luna" src="https://img.shields.io/github/release/fortserver/luna.svg" /></a>                   | Веб-терминал fortserver                                                                                 |
| [KoKo](https://github.com/fortserver/koko)             | <a href="https://github.com/fortserver/koko/releases"><img alt="Выпуск Koko" src="https://img.shields.io/github/release/fortserver/koko.svg" /></a>                   | Коннектор протокола символов fortserver                                                                 |
| [Lion](https://github.com/fortserver/lion)             | <a href="https://github.com/fortserver/lion/releases"><img alt="Выпуск Lion" src="https://img.shields.io/github/release/fortserver/lion.svg" /></a>                   | Коннектор графического протокола fortserver                                                             |
| [Chen](https://github.com/fortserver/chen)             | <a href="https://github.com/fortserver/chen/releases"><img alt="Выпуск Chen" src="https://img.shields.io/github/release/fortserver/chen.svg" />                       | Веб-база данных fortserver                                                                              |  
| [Tinker](https://github.com/fortserver/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Коннектор удаленного приложения fortserver (Windows)                                                  |
| [Panda](https://github.com/fortserver/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | Коннектор удаленного приложения fortserver EE (Linux)                                                  |
| [Razor](https://github.com/fortserver/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | Коннектор прокси RDP fortserver EE                                                                       |
| [Magnus](https://github.com/fortserver/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Коннектор прокси базы данных fortserver EE                                                                |
| [Nec](https://github.com/fortserver/nec)               | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | Коннектор прокси VNC fortserver EE                                                                       |
| [Facelive](https://github.com/fortserver/facelive)     | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | Коннектор распознавания лиц fortserver EE                                                                |


## Участие

Добро пожаловать, чтобы подать PR для участия. Пожалуйста, ознакомьтесь с [CONTRIBUTING.md][contributing-link] для получения рекомендаций.

## License

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