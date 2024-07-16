# Flaskサーバーのメインスクリプト
# chromeの拡張機能からのリクエストを受け取り、データベースに履歴保存
# server.py
################################################################################################
################################################################################################
################################################################################################

# import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime, timedelta
import csv
from init_db import init_db

app = Flask(__name__)
CORS(app)  # CORSを有効にしてクロスオリジンリクエストを許可

# アプリケーション起動時にデータベースを初期化
with app.app_context():
    init_db()

@app.route('/')
def index():
    return 'Browsing History Tracker Server is running.'

@app.route('/save_history', methods=['POST'])
def save_history():
    data = request.json
    conn = sqlite3.connect('browsing_history.db')
    c = conn.cursor()
    # ISO 8601形式のタイムスタンプをパースしてdatetimeオブジェクトに変換
    visit_time = datetime.fromisoformat(data['time'].replace('Z', '+00:00'))
    # データを改行付きで保存
    c.execute("INSERT INTO history (url, title, time) VALUES (?, ?, ?)",
              (data['url'], data['title'], visit_time))
    conn.commit()
    conn.close()
    # CSVファイルを更新
    update_csv()
    return jsonify({"status": "success"}), 200

def update_csv():
    conn = sqlite3.connect('browsing_history.db')
    c = conn.cursor()
    c.execute("SELECT url, title, time FROM history")
    rows = c.fetchall()
    conn.close()

    with open('browsing_history.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # ヘッダー行を書く
        csvwriter.writerow(['url', 'title', 'timestamp', 'subtraction'])
        previous_time = None
        for row in rows:
            current_time = datetime.fromisoformat(row[2])
            if previous_time:
                subtraction = (current_time - previous_time).total_seconds()
            else:
                subtraction = timedelta(0)
            csvwriter.writerow([row[0], row[1], row[2], str(subtraction)])
            previous_time = current_time

if __name__ == '__main__':
    app.run(debug=True)

# # read csv
# df = pd.read_csv('browsing_history.csv')
# print(df)

###############################################################################################
###############################################################################################
###############################################################################################
