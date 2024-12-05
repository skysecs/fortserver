<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.org/index-en.html"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Uma ferramenta PAM de código aberto (Bastion Host)

[![][license-shield]][license-link]
[![][discord-shield]][discord-link]
[![][docker-shield]][docker-link]
[![][github-release-shield]][github-release-link]
[![][github-stars-shield]][github-stars-link]

[English](/README.md) · [中文(简体)](/readmes/README.zh-hans.md) · [中文(繁體)](/readmes/README.zh-hant.md) · [日本語](/readmes/README.ja.md) · [Português (Brasil)](/readmes/README.pt-br.md)

</div>
<br/>

## O que é o fortserver?

fortserver é uma ferramenta de Gerenciamento de Acesso Privilegiado (PAM) de código aberto que fornece às equipes de DevOps e TI acesso sob demanda e seguro a SSH, RDP, Kubernetes, Banco de Dados e endpoints RemoteApp através de um navegador da web.

![Visão geral do fortserver](https://github.com/fortserver/fortserver/assets/32935519/35a371cb-8590-40ed-88ec-f351f8cf9045)

## Começando Rápido

Prepare um servidor Linux limpo (64 bits, >= 4c8g)

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Acesse o fortserver no seu navegador em `http://your-fortserver-ip/`
- Nome de usuário: `admin`
- Senha: `ChangeMe`

[![fortserver Começando Rápido](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "fortserver Começando Rápido")

## Capturas de Tela

<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="Console do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="Auditorias do fortserver"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="Banco de Trabalho do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="Configurações do fortserver"   /></td>
  </tr>

  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="SSH do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="RDP do fortserver"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="K8s do fortserver"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/fortserver/fortserver/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="DB do fortserver"   /></td>
  </tr>
</table>

## Componentes

fortserver consiste em múltiplos componentes-chave, que em conjunto formam a estrutura funcional do fortserver, fornecendo aos usuários capacidades abrangentes para gerenciamento de operações e controle de segurança.

| Projeto                                               | Status                                                                                                                                                                 | Descrição                                                                                             |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/fortserver/lina)            | <a href="https://github.com/fortserver/lina/releases"><img alt="Lina release" src="https://img.shields.io/github/release/fortserver/lina.svg" /></a>                   | Interface do Usuário Web do fortserver                                                                  |
| [Luna](https://github.com/fortserver/luna)            | <a href="https://github.com/fortserver/luna/releases"><img alt="Luna release" src="https://img.shields.io/github/release/fortserver/luna.svg" /></a>                   | Terminal Web do fortserver                                                                               |
| [KoKo](https://github.com/fortserver/koko)            | <a href="https://github.com/fortserver/koko/releases"><img alt="Koko release" src="https://img.shields.io/github/release/fortserver/koko.svg" /></a>                   | Conector do Protocolo de Caracteres do fortserver                                                       |
| [Lion](https://github.com/fortserver/lion)            | <a href="https://github.com/fortserver/lion/releases"><img alt="Lion release" src="https://img.shields.io/github/release/fortserver/lion.svg" /></a>                   | Conector do Protocolo Gráfico do fortserver                                                               |
| [Chen](https://github.com/fortserver/chen)            | <a href="https://github.com/fortserver/chen/releases"><img alt="Chen release" src="https://img.shields.io/github/release/fortserver/chen.svg" />                       | Banco de Dados Web do fortserver                                                                          |  
| [Razor](https://github.com/fortserver/razor)          | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                             | Conector Proxy RDP do fortserver EE                                                                      |
| [Tinker](https://github.com/fortserver/tinker)        | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                           | Conector de Aplicativo Remoto do fortserver EE (Windows)                                                |
| [Panda](https://github.com/fortserver/Panda)          | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Conector de Aplicativo Remoto do fortserver EE (Linux)                                                  |
| [Magnus](https://github.com/fortserver/magnus)        | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Conector Proxy de Banco de Dados do fortserver EE                                                        |
| [Nec](https://github.com/fortserver/nec)              | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | Conector Proxy VNC do fortserver EE                                                                       |
| [Facelive](https://github.com/fortserver/facelive)    | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | Reconhecimento Facial do fortserver EE                                                                    |


## Contribuindo

Bem-vindo para enviar PR para contribuir. Por favor, consulte [CONTRIBUTING.md][contributing-link] para diretrizes.

## Segurança

fortserver é um produto crítico para a missão. Por favor, consulte as Recomendações Básicas de Segurança para instalação e implantação. Se você encontrar quaisquer problemas relacionados à segurança, entre em contato conosco diretamente:

- Email: support@fortserver.com

## License

Copyright (c) 2014-2024 fortserver, All rights reserved.

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

<!-- Image link -->