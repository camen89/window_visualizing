import sqlite3
import csv

def update_csv():
    conn = sqlite3.connect('browsing_history.db')
    c = conn.cursor()
    c.execute("SELECT url, title, time FROM history")
    rows = c.fetchall()
    conn.close()

    # 3行n列のCSV形式で保存
    with open('browsing_history.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # 各エントリを3行で保存
        for row in rows:
            csvwriter.writerow(['url', row[0]])
            csvwriter.writerow(['title', row[1]])
            csvwriter.writerow(['timestamp', row[2]])
            csvwriter.writerow([])  # 空行を追加してエントリ間を区切る

if __name__ == '__main__':
    update_csv()
