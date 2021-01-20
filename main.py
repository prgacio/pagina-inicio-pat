from flask import Flask, render_template
import requests
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
Bootstrap(app)

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
UNSPLASH_SECRET_KEY = os.environ.get("UNSPLASH_SECRET_KEY")

UNSPLASH_ENDPOINT = "https://api.unsplash.com/photos/random"

@app.route("/")
def home():
    reponse = requests.get(
        UNSPLASH_ENDPOINT,
        params={"client_id": f"{UNSPLASH_ACCESS_KEY}", "query": "marrakech", "count": 3}
    )
    data = reponse.json()
    urls = [dictionary["urls"]["small"] for dictionary in data]
    print(urls)

    return render_template("index.html", photo_urls=urls)


if __name__ == "__main__":
    app.run()