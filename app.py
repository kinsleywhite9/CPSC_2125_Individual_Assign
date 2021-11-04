from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

if __name__ == "__main__":
    app.run(debug = True)