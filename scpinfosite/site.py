from quart import Quart, render_template, redirect, url_for
from discord.ext import ipc

app = Quart(__name__)
# secret_key must be the same as your server
ipc_client = ipc.Client(secret_key="scpinfoepic23")


@app.route("/")
async def home():
    return await render_template("index.html")


@app.route("/about")
async def about():
    return await render_template("about.html")


@app.route("/privacy")
async def privacy():
    return await render_template("privacy.html")


@app.route("/stats")
async def stats():
    server_count = await ipc_client.request("get_server_count")

    return await render_template("stats.html", servers=server_count)


if __name__ == "__main__":
    app.run(debug=True)
