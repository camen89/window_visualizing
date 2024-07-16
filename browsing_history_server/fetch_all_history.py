# import sqlite3

# def fetch_all_history():
#     conn = sqlite3.connect('browsing_history.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM history")
#     rows = c.fetchall()
#     for row in rows:
#         print(f"URL: {row[1]}\nTitle: {row[2]}\nTime: {row[3]}\n")
#     conn.close()

# if __name__ == '__main__':
#     fetch_all_history()


import sqlite3

def fetch_all_history():
    conn = sqlite3.connect('browsing_history.db')
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()
    for row in rows:
        print(f"URL: {row[1]}\nTitle: {row[2]}\nTime: {row[3]}\n")
    conn.close()

if __name__ == '__main__':
    fetch_all_history()
