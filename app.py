from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    print("i")
    return render_template("index.html")

@app.route("/joueurs")
def joueurs():
    print("j")
    return render_template("joueurs.html")

@app.route("/enationale/")
def enationale():
    print("n")
    return render_template("enationale.html")
