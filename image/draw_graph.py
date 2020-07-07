import numpy as np
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

file_sqlite3 = "../db/Yokosuga-time.db"
conn = sqlite3.connect(file_sqlite3)

df=pd.read_sql_query('SELECT * FROM sample', conn)
#date = '20' + df['年'].astype(str) + '/' + df['月'].astype(str) + '/' + df['日'].astype(str)


for num in range(366):
    month_n = df.iloc[num,2]
    if month_n < 10:
        month_n = '0' + str(month_n)
    elif month_n >= 10:
        month_n = str(month_n)
    day_n = df.iloc[num,3]
    if day_n < 10:
        day_n = '0' + str(day_n)
    elif day_n >= 10:
        day_n = str(day_n)
    date_n = '20' + str(df.iloc[num,1]) + '/' + month_n + '/' + day_n
    filename_n = month_n + day_n + '.png'

    x = df.columns[4:27]
    y = df.iloc[num,4:27]
    plt.figure(figsize=(20,10), dpi=50)
    plt.plot(x, y, color= 'blue')
    plt.title("Tide level of " + date_n)
    plt.xlabel("O'clock")
    plt.ylabel("cm")
    plt.grid(True)
    # image/Oarai
    plt.savefig("../image/Yokosuga/" + filename_n)
    #plt.show()
