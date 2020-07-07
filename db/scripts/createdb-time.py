import sqlite3
import pandas as pd

df = pd.read_csv("Yokosuga-time.csv")

dbname = "Yokosuga-time.db"

conn = sqlite3.connect(dbname)
cur = conn.cursor()

df.to_sql('sample', conn, if_exists='replace')

# 作成したデータベースを1行ずつ見る
select_sql = 'SELECT * FROM sample'
for row in cur.execute(select_sql):
    print(row)

cur.close()
conn.close()
