from flask import Flask,render_template

app = Flask(__name__)
posts=[

    {
        "author":"Solomon Ansah",

        "title":"Blog Post",

        "content": "My First Blog",

        "date": "April 20, 2021"

    },   
    {
        "author":"Jayden Ansah",

        "title":"Blog Post2",

        "content": "My Second Blog",

        "date": "May 20, 2021"


    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
