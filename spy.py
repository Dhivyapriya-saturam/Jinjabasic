from flask import Flask, render_template

app = Flask(__name__)


@app.route("/gret")
def greet():
    return render_template('forloop.html')


if __name__ == "__main__":
    app.run()
