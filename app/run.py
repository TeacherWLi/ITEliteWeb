"""

"""
__author__ = 'W. Li (liw@sicnu.edu.cn)'


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/')
def index():
    return render_template('index.html')
    #return '<html><body><h1>123<h1></body></html>'


@app.route('/login')
def login():
    return render_template('login.html')
    #return 'Login Page'


app.run(debug='True')   # 运行Web服务器


