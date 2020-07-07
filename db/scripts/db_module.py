# 長数字分解メソッド:solve
# numはデータの文字列, indexは数字
# num = データ文字列
# list = 分解数値代入用配列
def solve(num, list):
    # 残りの数字が3桁以内なら
    if len(num) <= 3:
        list.append(num)
        return list

    if num[0] == "1":
        # 0, 1, 2番目を取り出して足す
        cut = str(num[:3])
        list.append(cut)
        # [3]番目を見る
        num = num[3:]
        #print(cut)
        solve(num, list)
    # 先頭の文字が - だったとき
    elif num[0] == "-":
        # 2文字目が "1" なら
        if num[1] == "1":
            # 0, 1, 2番目を足す
            cut = str(num[:3])
            list.append(cut)
            # 3番目以降を次に渡す
            num = num[3:]
            solve(num, list)
        else:
            cut = str(num[:2])
            list.append(cut)

            num = num[2:]
            solve(num, list)

    else:
        # 先頭の数字が一桁で, 次が "-" の場合
        if num[1] == "-":
            cut = str(num[:1])
            list.append(cut)

            num = num[1:]
            solve(num, list)

        else:
            cut = str(num[:2])
            list.append(cut)
            # [2]番目を見る
            num = num[2:]
            #print(cut)
            solve(num, list)

    return list
