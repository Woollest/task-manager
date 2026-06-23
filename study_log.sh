# 1. ログを保存するディレクトリ（フォルダ）のパスを指定
LOG_DIR="/workspaces/working/logs"

# 2. ログを保存するディレクトリが存在しない場合は作成
mkdir -p "$LOG_DIR"

# 3. ログファイルの名前を指定（例: study_log_YYYYMMDD）
TODAY=$(date +%Y%m%d)
LOG_FILE="$LOG_DIR/study_log_$TODAY"

# 4. ログを保存する内容を指定（例: 学習内容や時間）
if [ -z "$1" ]; then
    cat << EOF > "$LOG_FILE"
# 学習ログ

## 学習時間
-

## 学習内容
-
EOF
    echo "学習ログを作成しました: $LOG_FILE"
else
    echo "今日の学習ログはすでに存在します: $LOG_FILE"
fi

# 5. ログファイルを開く
code "$LOG_FILE"