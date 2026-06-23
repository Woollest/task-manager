import sys
import json
import os
from datetime import datetime

# データの保存先ファイル
LOG_FILE = "study_log.json"

def load_logs():
    """ログファイルからデータを読み込む"""
    if not os.path.exists(LOG_FILE):
        print("ログファイルが見つかりません。")
        return []
    
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("ログファイルの読み込みに失敗しました。")
        return []
    
def save_logs(logs):
    """データをログファイルに保存する"""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=4)

def add_log(content, minutes):
    """新しい学習ログを追加する"""
    logs = load_logs()

    # 新しいレコードを作成
    new_record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "content": content,
        "minutes": minutes,
    }
    logs.append(new_record)
    save_logs(logs)
    print(f"学習ログを追加しました: {content} - {minutes}分")

def list_logs():
    """すべての学習ログを表示する"""
    logs = load_logs()

    if not logs:
        print("学習ログがありません。")
        return
    
    print("\n --- 学習ログ ---")
    for i, log in enumerate(logs, 1):
        print(f"{i}. [{log['date']}] {log['content']} : {log['minutes']}分")
    print("-----------------------\n")

def show_total_time():
    """総学習時間を表示する"""
    logs = load_logs()

    # リスト内包表記を使用して総学習時間を計算
    total_minutes = sum(log["minutes"] for log in logs)

    # 時間と分に変換
    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"総学習時間: {total_minutes}分 ({hours}時間 {minutes}分)")

def print_help():
    """ヘルプメッセージを表示する"""
    print("使い方を間違えています。以下のコマンドを使用してください:")
    print("  python study_log.py add \"学習内容\" 学習時間(分) ")
    print("  python study_log.py list")
    print("  python study_log.py total")

def main():
    """メイン関数"""
    # コマンドライン引数の数をチェック
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    # コマンドに応じて処理を分岐
    if command == "add":
        if len(sys.argv) < 4:
            print("エラー: 学習内容と学習時間を指定してください。")
            print_help()
            return
        content = sys.argv[2]
        try:
            minutes = int(sys.argv[3])
        except ValueError:
            print("エラー: 学習時間は整数で指定してください。")
            return
        add_log(content, minutes)
    elif command == "list":
        list_logs()
    elif command == "total":
        show_total_time()
    else:
        print_help()

if __name__ == "__main__":
    main()