from flask import Flask ,request
from flask import url_for
from flask import render_template

app = Flask(__name__)

name="andres"

# routes
@app.route("/")
def index():
    return render_template('hello.html', name=name)

@app.route("/process", methods=['GET', 'POST'])
def process():
    text = request.args.get('text')
    text = "el valor que viene del form es : " + text
    return "<h1>" + text + "</h1>" + "<a href='http://localhost:8080/'>Volver a la pagina principal</a>" 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)