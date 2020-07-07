#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
#print ("Content-Type: text/html\n\n")

import sqlite3
import sys
import io
import os
def flatten(nested_list):
    # 深さ優先探索の要領で入れ子のリストをフラットにする関数
    # フラットなリストとフリンジを用意
    flat_list = []
    fringe = [nested_list]

    while len(fringe) > 0:
        node = fringe.pop(0)
        # ノードがリストであれば子要素をフリンジに追加
        # リストでなければそのままフラットリストに追加
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list


# 数値バリデーション
# ・負数, 0

# 挿入するグラフ画像の日付番号を指定
def image_num(date):
    num = ''
    if int(date) >= 10:
        num += str(date)
    else:
        num += "0"
        num += str(date)
    return num

# データを取り出すメソッド
def db_process(filename, month1, day1, month2, day2):
    # Create a 'Connection' object.
    #print(filename)

    conn = sqlite3.connect('/home/kanta/public_html/shiohigari_app/db/'+filename)

    # Create a 'Cursor' object from 'Connection' object.
    cur = conn.cursor()
    data = []

    # SQL文

    # (1)month1 = month2の場合
    if month1 == month2:
        d1 = conn.cursor().execute("SELECT * FROM sample WHERE 月 == ? AND 日 >= ? AND 日 <= ? ", (month1, day1, day2))
        data.append(d1)



    # (2)month1 > month2の場合
    elif month2 == str(int(month1)+1):
        d1 = conn.cursor().execute("SELECT * FROM sample WHERE 月 == ? AND 日 >= ?", (month1, day1))
        data.append(d1)

        d2 = conn.cursor().execute("SELECT * FROM sample WHERE 月 == ? AND 日 <= ?", (month2, day2))
        data.append(d2)
    # (3)month1 > month2+1の場合
    else:
        d1 = conn.cursor().execute("SELECT * FROM sample WHERE 月 == ? AND 日 >= ?", (month1, day1))
        data.append(d1)

        d2 = conn.cursor().execute("SELECT * FROM sample WHERE 月 > ? AND 月 < ?", (month1, month2))
        data.append(d2)

        d3 = conn.cursor().execute("SELECT * FROM sample WHERE 月 == ? AND 日 <= ?", (month2, day2))
        data.append(d3)

    data = flatten(data)
    data_list = []
    for rows in data:
        for row in rows:
            if row[16]-2 >= 6 and row[16]+2 <= 17:
                data_list.append(row)
    return data_list
