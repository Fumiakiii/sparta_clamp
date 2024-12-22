from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/clock")
def clock():
    return render_template("clock.html")


@app.route("/level1")
def level1():
    return render_template("level1.html")


@app.route("/level2")
def level2():
    return render_template("level2.html")


@app.route("/level3")
def level3():
    return render_template("level3.html")


@app.route('/clock1')
def clock1():
    return render_template('clock1.html')


if __name__ == "__main__":
    app.run(debug=True)
