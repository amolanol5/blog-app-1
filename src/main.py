from flask import Flask

app = Flask(__name__)

#routes
@app.route("/")
def index():
    return "This is my Blog app"

@app.route("/files")
def files():
    return "This is the web of my files"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)