from flask import Flask
from flask import render_template
import requests

response=requests.get("https://api.npoint.io/72b41f988b11bb4970a2").json()

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",data=response)

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/post/<id>")
def get_post(id):
    n=int(id)-1
    return render_template("getpost.html",data=response,n=n)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__=="__main__":
    app.run(debug=True)