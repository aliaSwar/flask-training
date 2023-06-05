from flask import Flask,render_template, url_for, request, redirect
import pandas as pd

data = pd.read_csv('C:/Users/ALIA/Desktop/python/Seattle2014.csv')
df=pd.DataFrame(data)
df.head(10)
app = Flask(__name__)

data=df.head(10)





# Pass the required route to the decorator.
@app.route("/search")
def hello():
    return render_template('search.html', data=data)


@app.route("/",methods=["POST","GET"])
def index():
    if request.method =="POST":
        search=request.form["search"]
        return  search
    else:
       return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)