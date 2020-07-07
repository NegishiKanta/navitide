#!/usr/bin/env python
# coding: utf-8


import sqlite3
import cgi
from datetime import datetime

# choi 以下の日付を返す
# 結果表示用html文書
html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
    <link rel="stylesheet" href="../style.css">
  </head>
  <body>
  <header class="header">
   
   <p>潮干狩りタイム</p>
   </header>
  <ul>
  %s
  </ul>
  </body>
</html>"""


content=''

form=cgi.FieldStorage()
choi_str=form.getvalue('choi', '')



# Create a 'Connection' object.
conn = sqlite3.connect('db/TEST.db')



# month_dataは月別にデータを入れた配列
month_data = []

# Create a 'Cursor' object from 'Connection' object.
cur = conn.cursor()

query = 'SELECT * FROM sample where ' + '(月 = ' + "1" + ' and ' +\
'引1高 <= ' + choi_str + ')' + ' or ' + '(月 = ' + "1" + ' and ' + '引2高 <= ' + choi_str + ')'

data = cur.execute(query)


for row in data:

    # 引き潮の時刻
    ebb = row[0:4]


    #ebb = [ebb[i: i+3] for i in range(0, len(ebb), 3)]
    #for e in ebb:

    url = "http://localhost:8080/cgi-bin/Oarai_date.py?month="+ str(ebb[2]) +"&day=" + str(ebb[3]) + "&submit=送信"
    # 個別ページへのリンク
    content+=u"<li><a href=%s>%d月%d日</a></li>" % (url, ebb[2], ebb[3])





print("Content-type: text/html;charset=utf-8\n")
# html文書のなかにcontentを代入(%s の位置)
print (html_body % content).encode('utf-8')
