import numpy as np
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
#%matplotlib inline

#df = pd.read_csv('./times.db', encoding='utf_8')

file_sqlite3 = "db/times.db"
conn = sqlite3.connect(file_sqlite3)

num = 8

df=pd.read_sql_query('SELECT * FROM sample', conn)
date = '20' + df['年'].astype(str) + '/' + df['月'].astype(str) + '/' + df['日'].astype(str)

x = df.columns[4:27]
y = df.iloc[num,4:27]
plt.figure(figsize=(20,10), dpi=50)
plt.plot(x, y, color= 'black')
plt.title("Tide level of 2020/01/09")
plt.xlabel("O'clock")
plt.ylabel("cm")
plt.grid(True)
plt.savefig("img_0109.png")
plt.show()
