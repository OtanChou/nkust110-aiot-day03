import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter

db = sqlite3.connect("nkustnews.db")
data = list()  #創造空串列，新資料可以Append進來
sql = "select title from news;"  #把所有標題(title)都列出來，要做文字雲
rows = db.execute(sql)
for row in rows:
    data.append(row[0])  #新資料Append進data串列
data = ";".join(data)  #將串列資料用分號(;)連在一起，導入新的data，此時新data資料型態變為字串(str)，取代舊的被遺棄的data(串列list)
#先處裡字典，再處理停用詞
jieba.load_userdict("dict.txt")  #先載入字典，避免特定關鍵字被切開
with open('stopWords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]  #將記事本的停用詞清理成串列
#設置迴圈將字典用字進入停用詞檢查，不重複通過才送入keyterms
keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!="" 
                and keyterm.strip()!=","]
text = ",".join(keyterms)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# 細節說明
# res = jieba.cut(data)  #用jieba切開，切完是interate不能print
# res = [w for w in res]  #用一個迴圈定義才能print