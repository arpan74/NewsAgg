from flask import Flask, render_template
import scrape
import requests

app = Flask(__name__)


@app.route("/")
def index():
    content = scrape.getContent()
    return content

if __name__ == "__main__":
    app.run(debug=True)



