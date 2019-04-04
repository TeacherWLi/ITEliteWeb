"""

"""
__author__ = 'W. Li (liw@sicnu.edu.cn)'


from flask import Flask


app = Flask(__name__)


@app.route('/hello/')
def hello():
    return "Hello World"


# app.add_url_rule('/hello', view_func=hello)


@app.route('/')
def index():
    return "Home Page"


@app.route('/login')
def login():
    return 'Login Page'


app.run()




