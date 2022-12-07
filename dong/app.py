from flask import Flask, redirect,render_template,request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://id:pw@cluster0.tydewmu.mongodb.net/?retryWrites=true&w=majority')
db = client.insertdb

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/learn")
def learn():
    posts = list(db.insertdb.find().sort("_id", -1))
    return render_template('learn.html', posts=posts)

@app.route("/send", methods = ['POST'])
def index_post():
    msg= request.form['input']   #html에서 input 박스에 들어있는 데이터 받아옴
    getip = request.remote_addr 
    ip = '.'.join(getip.split('.')[:-2])    #ip받음
    doc = {'dbmsg':msg,'ip':ip}  #몽고db로 넘김
    if msg == " " in doc:
        return redirect('/learn')
    db.insertdb.insert_one(doc)
    return redirect('/learn')
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8000')
