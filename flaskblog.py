from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("templates/home.html")

@app.route("/about")
def about():
    return "<h1> Home Page</h1>"


if __name__=="__main__":
    app.run()
