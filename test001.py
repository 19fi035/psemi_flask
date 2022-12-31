from flask import Flask

app =Flask(__name__)

@app.route("/")
def hello():
    mes = "Hello World"
    return mes

    if __name__ == "__main__":
        app.run()
        