from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/vote")
def vote():
    return render_template("vote.html")


@app.route("/commands")
def commands():
    return render_template("commands.html")


if __name__ == "__main__":
    app.run(debug=True)
