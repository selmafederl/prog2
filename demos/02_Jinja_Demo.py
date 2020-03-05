from flask import Flask
from flask import render_template

app = Flask("Hello World")


@app.route('/hello')
def hello_world():
	return render_template('index.html', name="Selma")


@app.route("/test")
def test():
    return "success" #hier könnte man eine zweite Seite verlinken, um so auf die nächste Seite zu kommen

if __name__ == "__main__":
    app.run(debug=True, port=5000)
