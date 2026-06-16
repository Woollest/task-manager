# タスク管理ツール

このリポジトリは、シンプルな JSON ストレージを使ったコマンドラインタスク管理ツールです。

## 特徴

- タスクの追加、完了、削除、更新
- タスク一覧表示と検索
- 期限日・優先度・タグによる絞り込みとソート
- タスク統計の表示
- JSON ファイル保存（`tasks.json`）
- `tasks.json` は `.gitignore` で除外済み

## 必要環境

- Python 3.8 以上

## 使い方

このリポジトリのルートで次のコマンドを実行します。

```bash
python3 test.py --help
```

### タスク追加

```bash
python3 test.py add "タイトル" "説明" 2026-06-30 --priority high --tags test,cli
```

### タスク完了

```bash
python3 test.py complete 1
```

### タスク削除

```bash
python3 test.py delete 1
```

### タスク更新

```bash
python3 test.py update 1 --title "新タイトル" --description "新しい説明" --due_date 2026-07-01 --priority low --tags bug,urgent
```

### タスク一覧表示

```bash
python3 test.py list
```

フィルタ例:

```bash
python3 test.py list --pending --tag cli --sort priority
```

### タスク検索

```bash
python3 test.py search "キーワード"
```

### 統計表示

```bash
python3 test.py stats
```

## 保存先を変更する

`tasks.json` の代わりに別のファイルを使う場合:

```bash
python3 test.py --storage ./my_tasks.json add "タイトル" "説明" 2026-06-30
```

## 補足

- `tasks.json` はローカルのタスク状態保存用です。
- すでに Git 管理対象から外しているので、タスク操作による差分は発生しません。
