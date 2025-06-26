from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world' #請將 hello world 改成你最喜歡的一句話

@app.route('/name',methods = ['post'])
def get_form():
    data = request.json  #取得傳過來的資料(json格式)
    prompt = data.get('prompt') #取得prompt
    print(prompt)
    
    return jsonify({
            'status': 'success'
        })

app.run()

#reference：https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
#get (in line 12) reference：https://docs.python.org/zh-tw/3.13/library/stdtypes.html#dict.get
