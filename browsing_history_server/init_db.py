# データベースの初期化を行う
# SQLiteデータベースを作成
# ブラウジング履歴を保存するためのテーブル設定

import sqlite3

def init_db():
    conn = sqlite3.connect('browsing_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (url TEXT, title TEXT, time TIMESTAMP)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
