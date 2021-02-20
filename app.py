from flask import Flask, render_template, make_response,jsonify

import sqlite3
from wordcloud import WordCloud

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/index')
def home():
    # return render_template("index.html")
    return index()

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template("movie.html",movies = datalist)

@app.route('/word')
def word():
    return render_template("word.html")
@app.route('/team')
def team():
    return render_template("team.html")
@app.route('/score')
def score():
    score = []  #评分
    num = []    #每个评分统计出的电影数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num)
@app.route('/login/navlist')
def navlist():
    data = [{
        "title": "新品饮料",
        "src": '/images/temp/c1.png'
    },
        {
            "title": "新品饮料",
            "src": '/images/temp/c2.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c3.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c4.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c5.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c6.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c7.png'
        },
        {
            "title": "新品饮料",
            "src": '/images/temp/c8.png'
        }
    ]
    return jsonify(data)

@app.route('/login/getProductList')
def getProductList():
    data = []
    for i in range(1,24):
        s = {
        "id":i,
        "name": "华为Mate 30Pro ",
        "src": '/images/temp/cate'+str(i)+'.jpg',
        "price":4099-i*30
    }
        data.append(s)

    return jsonify(data)
@app.route('/slogin')
def slogin():
    response = make_response('true')
    return response

if __name__ == '__main__':
    app.run()
