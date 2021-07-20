from flask import Flask, render_template, url_for, redirect

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

@app.route("/invite")
def invite():
    return redirect("https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot", code=302)


@app.route("/commands")
def commands():
    return render_template("commands.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


if __name__ == "__main__":
    app.run(debug=True)
