from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

name="andres"

# routes
@app.route("/")
def index():
    return render_template('hello.html', name=name)

@app.route("/files")
def files():
    return "This is the web of my files"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('files'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)