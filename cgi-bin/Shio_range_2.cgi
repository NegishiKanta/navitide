#!/usr/bin/env python3
#print ("Content-Type: text/html\n")
# coding: utf-8
import cgitb
cgitb.enable()
import sqlite3
import cgi
from datetime import datetime
from cgi_module import flatten
from cgi_module import db_process

import html_str
import sys
import io
import os
form=cgi.FieldStorage()
month1=form.getvalue('month1', '')
day1=form.getvalue('day1', '')

month2=form.getvalue('month2', '')
day2=form.getvalue('day1', '')

spot = form.getvalue('sp1', '')
page=form.getvalue('page', '')


content=''
footer=''


# データ表示の始点・終点
start = (int(page) - 1)*7
finish = int(page)*7

# 地域名+.db でデータベースファイル名を設定
dbname=spot+'.db'
data_list = db_process(dbname, month1, day1, month2, day2)

# データ総数が7の倍数なら
if len(data_list) % 7 == 0:
    #
    page_sum = len(data_list) / 7

else:
    page_sum = len(data_list) / 7 + 1

data_list = data_list[start:finish]

for row in data_list:
    # 個別ページに月と日を渡す
    data_url = "http://160.16.107.107/~kanta/shiohigari_app/cgi-bin/Shio_date.cgi?sp1=%s&month=%s&day=%s&page=%s" % (spot, row[2], row[3], 1)
    # 個別ページへのリンク (日時・潮タイム)
    # 制限: 6時~18時まで => row[16]-2 >= 8, row[16]+2 <= 16:

    content+=u"<tr><td><a href=%s>%d/%d/2020</a></td>" % (data_url+"&submit=%E9%80%81%E4%BF%A1", row[3], row[2])
    if len(str(row[17])) == 1:
        content+=u"<td>%d:%s~%d:%s</td>" % (row[16]-2, "0"+str(row[17]), row[16], "0"+str(row[17]))
    else:
        content+=u"<td>%d:%d~%d:%d</td>" % (row[16]-2, row[17], row[16]+2, row[17])
    # もし干潮-2 が存在すれば row[18]
    if row[19] != 99 and row[19]-2 >= 6 and row[19]+2 <= 17:
        content+=u"<td>%d/%d~%d/%d</td></tr>" % (row[19]-2, row[20], row[19]+2, row[20])
    else:
        content+=u"<td></td></tr>"

# このページの次のページ番号
next_page = int(page) + 1
# このページの前のページ番号
pre_page = int(page) - 1


# 前のページへ :footer
# ・3ページ目以上, ・2ページ目, ・1ページ目で分ける
if int(page) > 2:
    pre_url = "http://160.16.107.107/~kanta/shiohigari_app/cgi-bin/Shio_range_2.cgi?sp1=%s&month1=%s&day1=%s&month2=%s&day2=%s&page=%s"\
    % (spot, month1, day1, month2, day2, pre_page)
else:
    pre_url = "http://160.16.107.107/~kanta/shiohigari_app/cgi-bin/Shio_range_1.cgi?sp1=%s&month1=%s&day1=%s&month2=%s&day2=%s&page=%s"\
    % (spot, month1, day1, month2, day2, pre_page)
# 前のページへ
footer+=u"<th><a href=%s>Pre Page</a></th>" % (pre_url+"&submit=%E9%80%81%E4%BF%A1")

# 次のページへ :footer
if int(page) < page_sum - 1:
    next_page = int(page) + 1
    page_url = "http://160.16.107.107/~kanta/shiohigari_app/cgi-bin/Shio_range_2.cgi?sp1=%s&month1=%s&day1=%s&month2=%s&day2=%s&page=%s" % (spot, month1, day1, month2, day2, next_page)
    footer+=u"<th><a href=%s>Next Page</a></th>" % (page_url+"&submit=%E9%80%81%E4%BF%A1")





print("Content-type: text/html;charset=utf-8\n")
# html文書のなかにcontentを代入(%s の位置)
print (html_str.html_body % (content, footer))
