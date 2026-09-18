<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## Plataforma PAM de código abierto (bastión)

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

## ¿Qué es fortserver?

fortserver es una plataforma de gestión de accesos privilegiados (PAM) de código abierto con funciones de IA. Ofrece a los equipos de DevOps y TI un espacio de trabajo unificado para acceder de forma segura a SSH, RDP, Kubernetes, bases de datos, sitios web, RemoteApp, VirtualApp y otros recursos.

<img alt="Diagrama de arquitectura de fortserver" src="assets/fortserver-architecture.png" />

## Inicio rápido

Prepare un servidor Linux de 64 bits limpio, con al menos 4 núcleos de CPU y 8 GB de RAM.

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

Abra fortserver en el navegador en `http://your-fortserver-ip/`

- Usuario: `admin`
- Contraseña: `ChangeMe`

## Capturas de pantalla

<p align="center">
  <img src="assets/screenshot-01.png" alt="Panel de PAM de fortserver" width="49%" />
  <img src="assets/screenshot-02.png" alt="Gestión de activos de fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-03.png" alt="Diálogo de conexión SSH de fortserver" width="49%" />
  <img src="assets/screenshot-04.png" alt="Consulta a la IA desde el terminal de fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-05.png" alt="Asistente de IA de fortserver" width="49%" />
  <img src="assets/screenshot-06.png" alt="Sesión de escritorio remoto de fortserver" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-07.png" alt="Panel de activos del terminal de fortserver en tema claro" width="49%" />
  <img src="assets/screenshot-08.png" alt="Sesión SSH de fortserver en tema claro" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-09.png" alt="Panel de activos del terminal de fortserver en tema oscuro" width="49%" />
  <img src="assets/screenshot-10.png" alt="Sesión SSH de fortserver en tema oscuro" width="49%" />
</p>

## Componentes

Los componentes de fortserver se organizan según su función. Los proyectos principales proporcionan la plataforma, la interfaz web, la terminal, las conexiones de protocolo y las funciones de IA. Los componentes empresariales amplían el acceso a aplicaciones y protocolos. Los servicios auxiliares gestionan las grabaciones de sesiones y las operaciones de los hosts, mientras que las herramientas de despliegue facilitan la instalación y la entrega web.

### Proyectos principales

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Proyecto</th>
      <th width="135" align="center"><div align="center">Versión</div></th>
      <th width="550" align="center"><div align="center">Descripción</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/fortserver">fortserver</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/fortserver/tags"><img src="https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&amp;filter=v5.*&amp;label=tag" alt="fortserver versión" /></a></div></td>
      <td width="550" align="left">Plataforma de gestión de accesos privilegiados de código abierto</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/lina">Lina</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/lina/tags"><img src="https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Lina versión" /></a></div></td>
      <td width="550" align="left">Interfaz web de fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/luna">Luna</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/luna/tags"><img src="https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Luna versión" /></a></div></td>
      <td width="550" align="left">Terminal web y cliente nativo de fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/koko">KoKo</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/koko/tags"><img src="https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&amp;filter=v5.*&amp;label=tag" alt="KoKo versión" /></a></div></td>
      <td width="550" align="left">Conector y proxy de protocolos de uso general de fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/chen">Chen</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/chen/tags"><img src="https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Chen versión" /></a></div></td>
      <td width="550" align="left">Conector de bases de datos web de fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/kael">Kael</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/kael/tags"><img src="https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Kael versión" /></a></div></td>
      <td width="550" align="left">Componente de IA de fortserver</td>
    </tr>
  </tbody>
</table>

### Componentes empresariales

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Proyecto</th>
      <th width="135" align="center"><div align="center">Versión</div></th>
      <th width="550" align="center"><div align="center">Descripción</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/tinker">Tinker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Conector de aplicaciones Windows de fortserver (gratuito en la edición Community)</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/Panda">Panda</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Conector de aplicaciones Linux de fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/razor">Razor</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Proxy del protocolo RDP de fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/magnus">Magnus</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Proxy de protocolos de bases de datos de fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/nec">Nec</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Proxy del protocolo VNC de fortserver Enterprise Edition</td>
    </tr>
  </tbody>
</table>

### Servicios auxiliares

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Proyecto</th>
      <th width="135" align="center"><div align="center">Versión</div></th>
      <th width="550" align="center"><div align="center">Descripción</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/video-worker">Video&nbsp;Worker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Servicio de transcodificación de grabaciones de sesiones de fortserver Enterprise Edition</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/jdmc">JDMC</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="Versión privada" /></div></td>
      <td width="550" align="left">Servicio de operaciones y administración de hosts de fortserver Enterprise Edition</td>
    </tr>
  </tbody>
</table>

### Despliegue y herramientas

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">Proyecto</th>
      <th width="135" align="center"><div align="center">Versión</div></th>
      <th width="550" align="center"><div align="center">Descripción</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/installer">Installer</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/installer/tags"><img src="https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Installer versión" /></a></div></td>
      <td width="550" align="left">Herramienta de instalación y administración de fortserver</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/docker-web">Docker&nbsp;Web</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/docker-web/tags"><img src="https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Docker Web versión" /></a></div></td>
      <td width="550" align="left">Puerta de enlace web y recursos estáticos de fortserver</td>
    </tr>
  </tbody>
</table>

## Contribuir

Se agradecen las contribuciones. Consulte [CONTRIBUTING.md][contributing-link] para conocer las directrices.

## Licencia

Copyright (c) 2014-2026 fortserver. Todos los derechos reservados.

Este proyecto se distribuye bajo la Licencia Pública General de GNU, versión 3 (GPLv3, la «Licencia»). Solo puede utilizar este archivo de conformidad con la Licencia. Puede obtener una copia en

https://www.gnu.org/licenses/gpl-3.0.html

Salvo que lo exija la ley aplicable o se acuerde por escrito, el software distribuido bajo la Licencia se proporciona «TAL CUAL», SIN GARANTÍAS NI CONDICIONES DE NINGÚN TIPO, expresas o implícitas. Consulte la Licencia para conocer los permisos y las limitaciones específicos.

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
