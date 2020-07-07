# coding: UTF-8
# 気象庁のtxtファイルをcsvに変換
import re
import csv
import sqlite3


f = open('tokyo.txt')
lines = f.readlines()
# 一行目に挿入するヘッダー
head = ["年", "月", "日", "満1時", "満1分", "満1高", "満2時", "満2分", "満2高", "満3時", \
"満3分", "満3高", "満4時", "満4分", "満4高", "引1時", "引1分", "引1高", "引2時", "引2分", \
"引2高", "引3時", "引3分", "引3高", "引4時","引4分","引4高"]

# res: csvに挿入するデータの2次元配列
res = [head]

for line in lines:
    result = []

    # 潮位を入れる配列
    choi = []


    split_list = re.split(r'TK', line)
    # shio: 日付, 満潮, 干潮のデータを入れる配列


    # shio: 日付, 満潮, 干潮のデータを入れる配列
    print(split_list)
    # split_list[0] から月と日を含む文字列のみ取得
    datestr = split_list[0][::-1][:6][::-1]
    print(datestr)

    year = datestr[:2]
    month = datestr[2:4]
    day = datestr[4:]


    choi.append(year)
    choi.append(month)
    choi.append(day)


    shio = split_list[1]
    # 満潮・干潮の数値を7文字ずつ区切る
    shio = [shio[i: i+7] for i in range(0, len(shio), 7)]
    # 空要素を削除
    shio = [x for x in shio if x]
    # 改行を削除
    shio.remove('\n')


    for value in shio:
        # time: 満潮・干潮の時刻
        time = value[:4]
        # 満潮・干潮時の潮位
        num = value[4:]

        hour = time[:2].split(" ")
        # 空要素を除く
        hour = [x for x in hour if x]


        min = time[2:].split(" ")
        min = [x for x in min if x]

        num = num.split(" ")
        num = [x for x in num if x]

        # 配列に挿入
        choi.append(hour[0])
        choi.append(min[0])
        choi.append(num[0])
        choi = [x for x in choi if x]

    result.append(choi)
    res.append(result[0])

# csvに書き込み
with open('tokyo.csv', 'w', encoding="utf_8_sig") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(res)
