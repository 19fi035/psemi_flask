import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# def hello():
#     mes = "Hello World"
#     return mes
def index():
    dictionary = {"food":"ラーメン","things":"映画鑑賞",}
    return render_template("index.html",list =list,dictionary=dictionary,)

if __name__ == "__main__":
    app.run(port=8080)