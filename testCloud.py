from wordcloud import WordCloud         #词云
import jieba                            #分词
from matplotlib import pyplot as plt    #绘图 数据可视化
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库


con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'./static/assets/img/tree2.jpg')
img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片

fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴

# plt.show()  #显示生成的词云图片
plt.savefig(r'.\static\assets\img\ntree2.jpg',dpi=500)
