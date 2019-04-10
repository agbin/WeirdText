from flask import Flask, render_template, request

import encoding

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("weird.html")


@app.route('/v1/encode', methods=['GET', 'POST'])
def encode():
    if request.method == "POST":
        sentence = request.form["text"]
        to_encode = encoding.garble(sentence)
        to_encode = to_encode.replace('\n', '<br>')
        return render_template("encode.html", to_encode=to_encode)
    return render_template("encode.html")


@app.route('/v1/decode', methods=['GET', 'POST'])
def decode():
    if request.method == "POST":
        encoded = request.form["encoded"]
        to_decode = encoding.decode(encoded)
        to_decode = to_decode.replace('\n', '<br>')
        return render_template("decode.html", to_decode=to_decode)
    return render_template("decode.html")


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == '__main__':
    app.run()
