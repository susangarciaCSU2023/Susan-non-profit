from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/page")
def page1():
    return render_template("donate.html")

@app.route("/shopping")
def page2():
    return render_template("shop.html")

if __name__ == "__main__":
    app.run()
 
