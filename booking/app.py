#from bottle import debug

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/home")

def home():
    return "<h1>home page</h1>"
    
    
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/rooms")
def rooms():
    return render_template("room.html")
    

if __name__ == '__main__':
 app.run(debug=True)

