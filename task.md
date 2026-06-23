# Webアプリ開発・IT学習ロードマップ

## 目標

このロードマップの最終目標は、以下のような現場寄りのWebアプリを自力で作れるようになることです。

> React + TypeScript + FastAPI + PostgreSQL + Docker Compose を使って、実用的なWebアプリを作成し、GitHubで公開できる状態にする。

AI開発ツールやClaude Codeは最初から丸投げするのではなく、基礎を理解したうえで補助として活用する方針です。

---

## 全体方針

- Webアプリ開発を軸にする
- Git / GitHubで成果物を管理する
- Linux / WSLを開発環境として使えるようにする
- React + TypeScriptでフロントエンドを作る
- FastAPIでバックエンドAPIを作る
- PostgreSQLでデータを管理する
- Docker Composeで開発環境を再現できるようにする
- セキュリティ・ネットワーク・低レイヤーは強みとして段階的に伸ばす
- Claude CodeなどのAIツールは補助として使う

---

# 学習ロードマップ

## 第0段階：学習環境を整える

### 学ぶこと

- Windows
- WSL2
- Ubuntu
- VS Code
- Git
- GitHub
- Docker Desktop
- Docker Compose
- Node.js
- Python
- PostgreSQL

### やること

- WSL2上で開発できるようにする
- VS CodeからWSLに接続する
- GitHubアカウントを整える
- Docker Composeで簡単なコンテナを起動する
- Windows側に開発環境を直接入れすぎず、WSL中心にする

### 目標

- Windows + WSL2 + Docker + VS Code の環境で開発できる
- GitHubにコードをアップロードできる準備ができている

---

## 第1段階：Git / GitHub

### 学ぶこと

- Gitとは何か
- commit
- branch
- merge
- push / pull
- GitHubへの公開
- READMEの書き方
- `.gitignore`
- コンフリクト解決
- Issue / Pull Requestの雰囲気

### やること

練習用リポジトリを作成する。

例：

```text
learning-log
```

中身の例：

```text
README.md
notes/
  git.md
  linux.md
  python.md
```

学習メモをGitHubにpushし、日々commitする習慣を作る。

### 目標

- GitHubに自分のリポジトリを作れる
- 変更をcommitできる
- branchを切れる
- READMEを書ける

### 目安時間

3〜5時間

---

## 第2段階：Linux基礎

LinuCレベル1の学習と並行して進める。

### 学ぶこと

- ディレクトリ操作
- ファイル操作
- 権限
- ユーザー・グループ
- プロセス
- パッケージ管理
- systemd
- ネットワーク確認
- ssh
- shell script基礎
- grep / find / sed / awk の基礎

### やること

WSL上で実際にコマンドを打ちながら、自分用チートシートを作成する。

例：

```text
linux-practice
```

中身の例：

```text
commands.md
permission.md
network.md
process.md
shell-script.md
```

簡単なシェルスクリプトも作る。

```bash
#!/bin/bash
echo "今日の学習ログを作成します"
date >> study.log
```

### 目標

- Linux上でファイル操作できる
- 権限の意味が分かる
- ログを見られる
- プロセスを確認できる
- shell scriptを少し書ける

### 目安時間

10〜20時間

---

## 第3段階：Python基礎

FastAPIに入る前に、Pythonの基本を固める。

### 学ぶこと

- 変数
- 条件分岐
- ループ
- 関数
- list / dict
- class
- ファイル読み書き
- 例外処理
- venv
- pip
- 型ヒント
- JSON操作

### やること

小さいCLIツールを作る。

例：

```text
学習記録CLI
```

機能例：

- 学習内容を追加
- 学習時間を記録
- JSONに保存
- 合計学習時間を表示

コマンド例：

```bash
python study_log.py add "FastAPI学習" 60
python study_log.py list
python study_log.py total
```

### 目標

- PythonでJSONを扱える
- 関数で処理を分けられる
- 簡単なツールを作れる

### 目安時間

10〜15時間

---

## 第4段階：JavaScript / TypeScript基礎

Reactを学ぶ前に、JavaScriptとTypeScriptの基礎を押さえる。

### 学ぶこと

#### JavaScript

- 変数
- 配列
- オブジェクト
- 関数
- map / filter / reduce
- Promise
- async / await
- fetch

#### TypeScript

- 型注釈
- interface
- type
- optional
- union
- genericsの基礎
- Reactで使うpropsの型

### やること

すでに作成したゲーム統計情報ツールを改善する。

改善例：

- TypeScript化
- データ型を定義
- JSON構造を整理
- 表示処理を関数に分ける
- READMEを書く

### 目標

- TypeScriptの型が分かる
- JSONデータを扱える
- async / awaitでデータ取得の雰囲気が分かる

### 目安時間

10〜20時間

---

## 第5段階：React

ここからフロントエンド開発に入る。

### 学ぶこと

- コンポーネント
- props
- state
- useState
- useEffect
- イベント処理
- フォーム
- React Router
- API通信
- CSS
- 状態管理の基礎
- Vite
- TypeScript React

### やること

Reactだけで完結するアプリを作る。

例：

```text
学習管理ダッシュボード
```

機能例：

- 学習項目一覧
- 学習時間登録
- 進捗率表示
- カテゴリ分類
- 検索
- JSONから読み込み
- localStorage保存

ここではまだバックエンドなしでよい。

### 目標

- Reactで画面を作れる
- フォーム入力を扱える
- コンポーネント分割できる
- TypeScriptでpropsを書ける

### 目安時間

20〜30時間

---

## 第6段階：FastAPI

バックエンドAPIの作成に入る。

### 学ぶこと

- APIとは何か
- HTTP
- GET / POST / PUT / DELETE
- ルーティング
- Pydantic
- バリデーション
- JSONレスポンス
- CORS
- uvicorn
- OpenAPI / Swagger UI
- エラーハンドリング

### やること

まずDBなしでAPIを作る。

例：

```text
study-api
```

API例：

```text
GET /tasks
POST /tasks
GET /tasks/{id}
PUT /tasks/{id}
DELETE /tasks/{id}
```

最初はメモリ上の配列やJSONファイル保存でよい。

### 目標

- FastAPIでAPIを作れる
- Swagger UIで動作確認できる
- ReactからAPIを呼べる
- CORSの意味が分かる

### 目安時間

10〜20時間

---

## 第7段階：React + FastAPI連携

フロントエンドとバックエンドをつなぐ。

### 学ぶこと

- フロントとバックエンドの分離
- API設計
- fetch / axios
- CORS
- エラー表示
- ローディング表示
- フォーム送信
- 状態更新

### やること

Reactの学習管理アプリをFastAPIにつなぐ。

構成例：

```text
frontend/
  React + TypeScript

backend/
  FastAPI
```

機能例：

- 学習記録一覧取得
- 学習記録追加
- 編集
- 削除
- 検索
- カテゴリ分類

### 目標

- ReactからFastAPIを呼べる
- CRUDの流れが分かる
- 画面とAPIを分けて考えられる

### 目安時間

15〜25時間

---

## 第8段階：DB / PostgreSQL

現場感を出すためにDBを扱う。

### 学ぶこと

- RDBとは何か
- テーブル
- 主キー
- 外部キー
- SELECT / INSERT / UPDATE / DELETE
- JOIN
- マイグレーション
- SQLAlchemy
- Alembic
- PostgreSQL

### やること

FastAPIの保存先をPostgreSQLに変える。

テーブル例：

```text
users
tasks
study_logs
categories
```

最初は認証なしでもよい。

### 目標

- DBにデータを保存できる
- FastAPIからDB操作できる
- テーブル設計の基本が分かる

### 目安時間

15〜30時間

---

## 第9段階：Docker / Docker Compose

開発環境を再現できる形にする。

### 学ぶこと

- Dockerとは何か
- image
- container
- Dockerfile
- docker compose
- volume
- network
- environment variables
- `.env`

### やること

React + FastAPI + PostgreSQLをDocker Composeで起動できるようにする。

構成例：

```text
project/
  frontend/
  backend/
  docker-compose.yml
  README.md
```

起動コマンド例：

```bash
docker compose up --build
```

### 目標

- Docker Composeで一発起動できる
- DBコンテナを使える
- 環境変数を使える
- READMEに起動手順を書ける

### 目安時間

10〜20時間

---

## 第10段階：認証・権限

ポートフォリオとして一段上げるため、認証機能を入れる。

### 学ぶこと

- 認証と認可の違い
- password hash
- JWT
- login
- logout
- protected route
- admin / user
- Cookie / localStorageの違い
- セキュリティの基本

### やること

ログイン機能を追加する。

機能例：

- ユーザー登録
- ログイン
- JWT発行
- ログイン中のユーザー取得
- 自分のデータだけ見られる
- 管理者だけ全件見られる

### 目標

- ログイン付きWebアプリを作れる
- 権限の概念が分かる
- セキュリティを意識できる

### 目安時間

15〜30時間

---

## 第11段階：本命の成果物を作る

練習アプリではなく、見せる用の成果物を作る。

# IT資産管理システム

## 技術構成

```text
Frontend: React + TypeScript
Backend: FastAPI
Database: PostgreSQL
Container: Docker Compose
Auth: JWT
Version Control: Git / GitHub
```

## 最低限の機能

- ログイン
- ユーザー管理
- PC資産登録
- 資産一覧
- 詳細表示
- 編集
- 削除
- 検索
- ステータス管理
- CSV出力
- README整備

## 資産情報の例

```text
管理番号
PC名
利用者
部署
OS
CPU
メモリ
ストレージ
IPアドレス
購入日
保証期限
状態
備考
```

## 発展機能

- 修理履歴
- 貸出・返却
- ソフトウェア管理
- 脆弱性メモ
- 管理者権限
- ダッシュボード
- グラフ表示
- CSVインポート
- 操作ログ

## なぜこの成果物が良いか

以下の学習内容とつながるため。

- Webアプリ開発
- Linux
- ネットワーク
- セキュリティ
- IT運用
- Tanium
- Entra ID
- AD
- 資産管理
- AI活用

単なるTODOアプリより、業務システムとして現場に近い。

---

## 第12段階：GitHub公開・README整備

作ったアプリを見せられる形にする。

### READMEに書くこと

- アプリ概要
- 作った理由
- 使用技術
- 機能一覧
- 画面スクリーンショット
- ER図
- API一覧
- ディレクトリ構成
- 起動方法
- テスト用アカウント
- 工夫した点
- 今後の改善点

### 使用技術の記載例

```text
## 使用技術

- React
- TypeScript
- FastAPI
- PostgreSQL
- Docker Compose
- SQLAlchemy
- Alembic
- JWT Authentication
```

### 目標

- GitHubを見ただけで何を作ったか分かる
- `docker compose up --build` で動く
- READMEが丁寧
- スクリーンショットがある
- 技術選定の理由が書いてある

---

## 第13段階：Claude Code / AI活用

基礎ができた後に、AI開発ツールを補助として使う。

### 学ぶこと

- AIに丸投げしない使い方
- 要件定義を渡す
- 既存コードを読ませる
- バグ調査をさせる
- テストを書かせる
- READMEを書かせる
- リファクタリングさせる

### やること

AIに以下のような作業を依頼する。

- コンポーネント分割の提案
- API設計レビュー
- DB設計レビュー
- README改善
- Dockerfile修正
- バグ原因の特定
- テストコード作成

### 方針

AIに全部作らせるのではなく、

> 自分が設計して、AIに補助させる

という使い方をする。

---

## 第14段階：ネットワーク・セキュリティ

Webアプリと並行して少しずつ学ぶ。

### 学ぶこと

- IPアドレス
- ポート
- DNS
- HTTP / HTTPS
- TLS
- Cookie
- Session
- JWT
- CORS
- SQLインジェクション
- XSS
- CSRF
- パスワードハッシュ
- ファイアウォール
- Linux権限
- SSH

### やること

自分のWebアプリに対して以下を確認する。

- CORS設定を理解する
- JWTの保存方法を考える
- パスワードをハッシュ化する
- SQLインジェクション対策を見る
- `.env`で秘密情報を管理する
- Dockerのポート公開を理解する

---

## 第15段階：C言語 / Ghidra / 低レイヤー

低レイヤー分野は、強みとして育てる。

### 学ぶこと

- C言語
- メモリ
- ポインタ
- スタック
- ヒープ
- ELF
- アセンブリ基礎
- Linux system call
- gdb
- objdump
- Ghidra
- バイナリ解析
- 脆弱性の基礎

### やること

小さいCプログラムを書いて、Ghidraやobjdumpで見る。

サンプル：

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    printf("%d\n", add(3, 5));
    return 0;
}
```

コンパイル例：

```bash
gcc main.c -o main
objdump -d main
```

### 仕事につながる分野

- セキュリティエンジニア
- 脆弱性診断
- マルウェア解析
- リバースエンジニアリング
- 組み込み開発
- Linuxカーネル周辺
- EDR / XDR / Tanium系の運用理解
- インフラ・セキュリティコンサル

未経験から最初の仕事につなげやすいのは、

> Web開発 + Linux + セキュリティ基礎

低レイヤーは、そこに足すことで個性・強みになる。

---

# おすすめの学習順まとめ

| 順番 | 内容 | 目的 |
|---:|---|---|
| 1 | Git / GitHub | 成果物を管理する |
| 2 | WSL / Linux基礎 | 開発環境とインフラ理解 |
| 3 | Python基礎 | FastAPIの土台 |
| 4 | JavaScript / TypeScript基礎 | Reactの土台 |
| 5 | React | フロント開発 |
| 6 | FastAPI | API開発 |
| 7 | React + FastAPI連携 | フルスタック理解 |
| 8 | PostgreSQL | DB理解 |
| 9 | Docker Compose | 現場っぽい起動構成 |
| 10 | 認証・権限 | 実務アプリ感を出す |
| 11 | IT資産管理システム制作 | ポートフォリオ |
| 12 | README・GitHub整備 | 見せる成果物にする |
| 13 | Claude Code活用 | 開発効率化 |
| 14 | セキュリティ・ネットワーク | 実務理解を深める |
| 15 | C / Ghidra / 低レイヤー | 強みとして伸ばす |

---

# 3か月プラン

## 1か月目：基礎固め

### やること

- Git / GitHub
- Linux基礎
- Python基礎
- JavaScript / TypeScript基礎

### 作るもの

- 学習ログCLI
- ゲーム統計ビューア改良版
- GitHub学習メモ

### 目標

- コードをGitHubに上げられる
- WSLで開発できる
- PythonとTypeScriptの基本が分かる

---

## 2か月目：Webアプリ基礎

### やること

- React
- FastAPI
- API通信
- CRUD
- PostgreSQL基礎

### 作るもの

- 学習管理アプリ
- FastAPI CRUD API
- React + FastAPI連携アプリ

### 目標

- 画面からAPIを呼べる
- DBに保存できる
- CRUDの流れが分かる

---

## 3か月目：ポートフォリオ制作

### やること

- Docker Compose
- 認証
- 権限
- README
- GitHub整備
- 軽いAI活用

### 作るもの

- IT資産管理システム

### 目標

- Docker Composeで一発起動
- ログイン機能あり
- DB保存あり
- READMEあり
- GitHubで見せられる

---

# 最初の成果物候補

## 1作目：学習ログCLI

### 技術

```text
Python
JSON
GitHub
```

### 目的

- Python基礎
- JSON操作
- GitHub練習

---

## 2作目：ゲーム統計ビューア改良版

### 技術

```text
React
TypeScript
JSON
Node.js
```

### 目的

- すでに作ったものを整理
- TypeScriptに慣れる
- READMEを書く

---

## 3作目：学習管理Webアプリ

### 技術

```text
React
TypeScript
FastAPI
JSON or SQLite
```

### 目的

- フロントとバックエンド連携
- CRUD理解

---

## 4作目：IT資産管理システム

### 技術

```text
React
TypeScript
FastAPI
PostgreSQL
Docker Compose
JWT
```

### 目的

- ポートフォリオ本命
- 現場っぽい成果物

---

# 1日の学習の進め方

毎回この流れで進める。

```text
1. 講座を見る
2. 手を動かして同じものを作る
3. 少しだけ自分用に改造する
4. GitHubにcommitする
5. READMEに学んだことを書く
```

ただ見るだけではなく、必ず自分用に少し改造する。

改造例：

- 表示項目を増やす
- バリデーションを追加する
- 検索機能を足す
- エラー表示を改善する
- UIを整える
- Docker対応する

---

# AIの使い方

## 使ってよいこと

- エラーの原因調査
- コードの解説
- READMEの改善
- 関数のリファクタリング
- テストケース作成
- 設計レビュー
- 学習計画の相談

## 最初は避けたいこと

- 要件だけ渡して全部作らせる
- 生成されたコードを読まずに貼る
- エラーの意味を理解せずに直す
- READMEまでAI任せで自分が説明できない

## 目指す状態

> AIも使いましたが、設計・DB構造・API仕様・認証の流れは自分で説明できます。

---

# 叔父さんに見せる成果物の説明例

```text
企業のPC・IT資産を管理するためのWebアプリです。
React + TypeScriptでフロントエンドを構築し、
FastAPIでREST APIを実装しました。
PostgreSQLにデータを保存し、Docker Composeで
開発環境を一括起動できるようにしています。
```

## 機能一覧の例

```text
- ユーザー登録・ログイン
- JWT認証
- PC資産の登録・編集・削除
- 資産一覧・詳細表示
- 検索・絞り込み
- 管理者権限
- CSV出力
- Docker Compose対応
```

---

# 最終目標

最終的には以下を満たす成果物を作る。

- React + TypeScriptで画面を作っている
- FastAPIでREST APIを作っている
- PostgreSQLでデータを保存している
- Docker Composeで一発起動できる
- JWT認証がある
- GitHubに公開している
- READMEが丁寧
- スクリーンショットがある
- ER図やAPI一覧がある
- 自分で設計意図を説明できる