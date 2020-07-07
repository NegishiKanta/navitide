# coding: UTF-8
import re
import csv
import sqlite3

# 各時間の潮位と日付をcsv=> databaseに格納

from db_module import solve



f = open('yokosuga.txt')
lines = f.readlines()
res = []

head = ["年", "月", "日", "0", "1", "2", "3", "4", "5", "6", \
"7", "8", "9", "10", "11", "12", "13", "14", "15", "16", \
"17", "18", "19", "20", "21","22","23"]

# res: csvに挿入するデータの2次元配列
res = [head]

for line in lines:
    # 潮位を入れる配列
    choi = []
    # print(line)
    # 文字列'D3'で区切る
    split_list = re.split(r'QN', line)


    # (1) 日付を取り出す
    # split_list[0] から月と日を含む文字列のみ取得
    datestr = split_list[0][::-1][:6][::-1]
    print(datestr)

    year = datestr[:2]
    month = datestr[2:4]
    day = datestr[4:]
    print(day, month, year)

    choi.append(year)
    choi.append(month)
    choi.append(day)



    # 空白でくぎる
    line = split_list[0]
    # listを一度反転し, 最初の５文字(日付部分をカット)
    line = line[::-1][6:][::-1]
    line = line.split(' ')
    #print(line)

    # 空要素を削除
    line = [x for x in line if x]
    #print(line)


    count = 0
    for num in line:
        # 潮位データが２文字のとき

        if len(num) == 2:
            choi.append(num)

        else:
            # 2文字以上だった場合
            list = solve(str(num), [])
            for element in list:
                choi.append(element)
                #print(len(choi))
                #print(choi)
        choi = choi[:27]
    res.append(choi)
    print(choi)

# csvに書き込み
with open('Yokosuga-time.csv', 'w', encoding="utf_8_sig") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(res)
