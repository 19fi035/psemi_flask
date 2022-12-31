from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
   str=’abc’
   list=[“a1”,”a2”,”a3”]
   dictionary={“name”:”John”,”age”:24}
   flag=True
return render_template('index_jinja.html',str=str,list=list,dictionary=dictionary,flag=flag)
if __name__ == "__main__":
app.run()