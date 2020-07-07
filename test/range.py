import sqlite3
def flatten(nested_list):
    """深さ優先探索の要領で入れ子のリストをフラットにする関数"""
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
content=''


month1="1"
day1="10"

month2="4"
day2="23"

page="3"
start = (int(page) - 1)*7
finish = int(page)*7
# Create a 'Connection' object.
conn = sqlite3.connect('db/TEST.db')


# Create a 'Cursor' object from 'Connection' object.
cur = conn.cursor()
# 'SELECT * FROM sample where 月 = 1'
data = []

d1 = conn.cursor().execute("SELECT * FROM sample WHERE (月 >= ? AND 日 >= ?) AND 月<= ?", (month1, day1, str(int(month1)+1)))
data.append(d1)
d2 = conn.cursor().execute("SELECT * FROM sample WHERE (月 > ? AND 月 < ?)", (month1, month2))
data.append(d2)
d3 = conn.cursor().execute("SELECT * FROM  sample  WHERE (月 <= ? AND 日 <= ?) AND 月 > ?", (month2, day2, str(int(month2)-1)))
data.append(d3)

data = flatten(data)

data_list = []

print(data)
count = 7 * page
for rows in data:
    for row in rows:
        data_list.append(row)

if page_sum = sum(data_list) % 7 == 0:
    page_sum = page_sum
else:
    page_sum += 1


data_list = data_list[start-1:finish]
for row in data_list:
    print(row)
