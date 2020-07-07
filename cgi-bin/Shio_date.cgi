#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
#print ("Content-Type: text/html\n\n")
import cgitb
cgitb.enable()
import sqlite3
import cgi
from datetime import datetime
from cgi_module import image_num
import sys
import io

html_body = '''
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
    <link rel="stylesheet" href="../stylesheet/style_date.css">
    <script src="https://use.fontawesome.com/releases/v5.3.1/js/all.js" defer ></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css" />
  </head>

  <body>
      <nav class="navbar is-success">
    <div class="navbar-brand">
      <a class="navbar-item" href="../form_range.html">
        <span>NAVITIDE</span>
      </a>
    </div>

    <div id="navbarExampleTransparentExample" class="navbar-menu">
      <div class="navbar-end">
        <a class="navbar-item" href="../form_range.html">
          Home
        </a>
        <a class="navbar-item" href="../about.html">
          About
        </a>

      </div>
    </div>
    </nav>

    <div class="date">Data of %s/2020</div>
    <table class="table">
    <tbody>
    <tr>
    <th>Recommended Time</th>
    <td>
    %s
    </td>
    </tr>

    <tr>
    <th>Ebb Time</th>
    <td>
    %s
    </td>
    </tr>

    <tr>
    <th>Ebb cm</th>
    <td>
    %s
    </td>
    </tr>

    </tbody>
    </table>

    <figure>
        <img src="../image/%s/%s.png">
    </figure>
    <figcaption>%s/2020  24hours Graph</figcaption>

  </body>
</html>'''




hikishio=''

kanchoi = ''

shio_time = ''


graph_name = ''

form=cgi.FieldStorage()
spot=form.getvalue('sp1', '')

month_str=form.getvalue('month', '')

month_str=form.getvalue('month', '')
day_str=form.getvalue('day', '')

date = '%s/%s' % (day_str, month_str)

# 挿入するグラフ画像の日付を指定
graph_name += image_num(month_str)
graph_name += image_num(day_str)


#!==
# Create a 'Connection' object.
dbname=spot+".db"
conn = sqlite3.connect('../db/'+dbname)

# Create a 'Cursor' object from 'Connection' object.
cur = conn.cursor()


# month, dateはフォームから受け取る
# SQL文でデータを取り出す
query = 'SELECT * FROM sample where 月 = %s and 日 = %s' % (month_str, day_str)
cur.execute(query)
#!==
ebb_list = []
for ebb in cur:
    # 引き潮の時刻
    # for ebb in row:
    # 潮位が999でないなら
    if ebb[18] != 999:
        time1 = ebb[16] - 2
        time2 = ebb[16] + 2
        if len(str(ebb[17])) == 1:
            hikishio+=u"%d:%s" % (ebb[16], "0"+str(ebb[17]))
        else:
            hikishio+=u"%d:%d" % (ebb[16], ebb[17])

        kanchoi += u"%dcm" % (ebb[18])
        if len(str(ebb[17])) == 1:
            shio_time += u"%d:%s~%d:%s" % (time1, "0"+str(ebb[17]), time2, "0"+str(ebb[17]))
        else:
            shio_time += u"%d:%d~%d:%d" % (time1, ebb[17], time2, ebb[17])




#print("Content-type: text/html;charset=utf-8\n")
# html文書のなかにcontentを代入(%s の位置)
print(html_body % (cgi.escape(date), cgi.escape(shio_time), cgi.escape(hikishio), cgi.escape(kanchoi), spot, cgi.escape(graph_name), cgi.escape(date)))
#print("\n")
