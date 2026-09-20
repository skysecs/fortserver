<div align="center">
  <a name="readme-top"></a>
  <a href="https://fortserver.com" target="_blank"><img src="https://download.fortserver.org/images/fortserver-logo.svg" alt="fortserver" width="300" /></a>
  
## オープンソースの特権アクセス管理（PAM）プラットフォーム（踏み台サーバー）

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

## fortserver とは？

fortserver は AI 機能を備えたオープンソースの特権アクセス管理（PAM）プラットフォームです。DevOps チームと IT チームが、SSH、RDP、Kubernetes、データベース、Web サイト、RemoteApp、VirtualApp などに安全にアクセスできる統合ワークスペースを提供します。

<img alt="fortserver の構成図" src="assets/fortserver-architecture.png" />

## クイックスタート

CPU 4 コア以上、メモリ 8 GB 以上のクリーンな 64 ビット Linux サーバーを用意してください。

```sh
curl -sSL https://github.com/fortserver/fortserver/releases/latest/download/quick_start.sh | bash
```

ブラウザーで fortserver にアクセスします： `http://your-fortserver-ip/`

- ユーザー名: `admin`
- パスワード: `ChangeMe`

## スクリーンショット

<p align="center">
  <img src="assets/screenshot-01.png" alt="fortserver の PAM ダッシュボード" width="49%" />
  <img src="assets/screenshot-02.png" alt="fortserver の資産管理" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-03.png" alt="fortserver の SSH 接続ダイアログ" width="49%" />
  <img src="assets/screenshot-04.png" alt="fortserver のターミナル AI への質問" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-05.png" alt="fortserver の AI アシスタント" width="49%" />
  <img src="assets/screenshot-06.png" alt="fortserver のリモートデスクトップセッション" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-07.png" alt="fortserver のライトテーマのターミナル資産パネル" width="49%" />
  <img src="assets/screenshot-08.png" alt="fortserver のライトテーマの SSH セッション" width="49%" />
</p>

<p align="center">
  <img src="assets/screenshot-09.png" alt="fortserver のダークテーマのターミナル資産パネル" width="49%" />
  <img src="assets/screenshot-10.png" alt="fortserver のダークテーマの SSH セッション" width="49%" />
</p>

## コンポーネント

fortserver のコンポーネントは役割ごとに分類されています。コアプロジェクトはプラットフォーム、Web UI、ターミナル、プロトコル接続、AI 機能を提供します。エンタープライズコンポーネントはアプリケーションとプロトコルへのアクセスを拡張します。補助サービスはセッション録画とホスト運用を担い、導入ツールはインストールと Web 配信を簡素化します。

### コアプロジェクト

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">プロジェクト</th>
      <th width="135" align="center"><div align="center">バージョン</div></th>
      <th width="550" align="center"><div align="center">説明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/fortserver">fortserver</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/fortserver/tags"><img src="https://img.shields.io/github/v/tag/fortserver/fortserver?sort=semver&amp;filter=v5.*&amp;label=tag" alt="fortserver バージョン" /></a></div></td>
      <td width="550" align="left">オープンソースの特権アクセス管理プラットフォーム</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/lina">Lina</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/lina/tags"><img src="https://img.shields.io/github/v/tag/fortserver/lina?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Lina バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の Web UI</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/luna">Luna</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/luna/tags"><img src="https://img.shields.io/github/v/tag/fortserver/luna?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Luna バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の Web ターミナルとネイティブクライアント</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/koko">KoKo</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/koko/tags"><img src="https://img.shields.io/github/v/tag/fortserver/koko?sort=semver&amp;filter=v5.*&amp;label=tag" alt="KoKo バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の汎用プロトコルコネクターとプロキシ</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/chen">Chen</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/chen/tags"><img src="https://img.shields.io/github/v/tag/fortserver/chen?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Chen バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の Web データベースコネクター</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/kael">Kael</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/kael/tags"><img src="https://img.shields.io/github/v/tag/fortserver/kael?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Kael バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の AI コンポーネント</td>
    </tr>
  </tbody>
</table>

### エンタープライズコンポーネント

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">プロジェクト</th>
      <th width="135" align="center"><div align="center">バージョン</div></th>
      <th width="550" align="center"><div align="center">説明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/tinker">Tinker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver の Windows アプリケーションコネクター（コミュニティ版では無料）</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/Panda">Panda</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版の Linux アプリケーションコネクター</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/razor">Razor</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版の RDP プロトコルプロキシ</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/magnus">Magnus</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版のデータベースプロトコルプロキシ</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/nec">Nec</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版の VNC プロトコルプロキシ</td>
    </tr>
  </tbody>
</table>

### 補助サービス

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">プロジェクト</th>
      <th width="135" align="center"><div align="center">バージョン</div></th>
      <th width="550" align="center"><div align="center">説明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/video-worker">Video&nbsp;Worker</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版のセッション録画トランスコードサービス</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/jdmc">JDMC</a></td>
      <td width="135" align="center"><div align="center"><img src="https://img.shields.io/badge/tag-private-red" alt="非公開バージョン" /></div></td>
      <td width="550" align="left">fortserver エンタープライズ版のホスト運用・管理サービス</td>
    </tr>
  </tbody>
</table>

### 導入とツール

<table width="100%">
  <thead>
    <tr>
      <th width="160" align="left">プロジェクト</th>
      <th width="135" align="center"><div align="center">バージョン</div></th>
      <th width="550" align="center"><div align="center">説明</div></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/installer">Installer</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/installer/tags"><img src="https://img.shields.io/github/v/tag/fortserver/installer?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Installer バージョン" /></a></div></td>
      <td width="550" align="left">fortserver のインストール・管理ツール</td>
    </tr>
    <tr>
      <td width="160" align="left" nowrap><a href="https://github.com/fortserver/docker-web">Docker&nbsp;Web</a></td>
      <td width="135" align="center"><div align="center"><a href="https://github.com/fortserver/docker-web/tags"><img src="https://img.shields.io/github/v/tag/fortserver/docker-web?sort=semver&amp;filter=v5.*&amp;label=tag" alt="Docker Web バージョン" /></a></div></td>
      <td width="550" align="left">fortserver の Web ゲートウェイと静的アセット</td>
    </tr>
  </tbody>
</table>

## コントリビューション

コントリビューションを歓迎します。手順については [CONTRIBUTING.md][contributing-link] を参照してください。

## ライセンス

Copyright (c) 2014-2026 fortserver. All rights reserved.

本プロジェクトは GNU General Public License バージョン 3（GPLv3、以下「ライセンス」）に基づいて提供されます。本ファイルはライセンスに従う場合にのみ使用できます。ライセンスの写しは次の URL で入手できます。

https://www.gnu.org/licenses/gpl-3.0.html

適用法令で義務付けられる場合、または書面で別途合意した場合を除き、ライセンスに基づいて配布されるソフトウェアは「現状有姿」で提供され、明示または黙示を問わず、いかなる保証や条件も伴いません。権利と制限の詳細はライセンスを参照してください。

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
