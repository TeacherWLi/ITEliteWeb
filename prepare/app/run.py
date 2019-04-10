"""

"""
__author__ = 'W. Li (liw@sicnu.edu.cn)'


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return "Hello World"


# app.add_url_rule('/hello', view_func=hello)


@app.route('/')
def index():
    return render_template("index.html", title_data='test')
    # return "<html><body><h1 align=\"center\">Home Page Header</h1></body></html>"
    # return "Home Page"


@app.route('/login')
def login():
    return render_template("longin.html")
    # return 'Login Page'


app.run(debug='True')




