import sqlite3
db = sqlite3.connect("nkustnews.db")
schools = ['台科','北科','雲科','屏科','中科'] #比較關鍵字出現次數
for school in schools:
    sql = "select count(*) from news where content like '%{}%';".format(school)
    rows = db.execute(sql)
    for row in rows:
        print("{}:{}次".format(school, row[0]))
# # sql = "select * from news;"
# # sql = "select * from news where id<30 order by id desc;"  #設條件id小於30，id由大到小排序
# # sql = "select id, title from news where content like '%台大%';" #出現台大關鍵字的新聞
# sql = "select id, title from news where content like '%台大%' order by date desc;" #出現台大關鍵字的新聞，date由近至遠
# # sql = "select count(*) from news where content like '%台大%';" #出現台大關鍵字的新聞數量
# rows = db.execute(sql)
# for row in rows:
#     print(row)
#     print(row[0])  #是row的第0個，不是rows的第0個