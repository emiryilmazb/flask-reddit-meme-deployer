from flask import Flask, render_template
import requests
import json

from flask import Flask

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-1]
    subreddit = response["subreddit"]
    title = response["title"]
    postlink = response["postLink"]
    return meme_large, subreddit, title, postlink


@app.route("/")
def index():
    meme_pic, subreddit, title, postlink = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit, title=title, postlink=postlink)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
