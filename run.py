html = """
<!doctype html>
<html>
<head>
</head>
<body bgcolor="ffbf00">
    <form action="/encode" method="POST">
        <input type="text" name="text" size="100" placeholder="Podaj tekst do zakodowania: ">
        <input type="submit" value="zakoduj">
    </form><br>
    <form action="/decode" method="POST">
        <input type="text" name="encoded" size="100" placeholder="Podaj tekst do odkodowania: ">
        <input type="submit" value="odkoduj">
    </form>
</body>                
</html>
"""



from flask import Flask, render_template, request, Response

import encoding

app = Flask(__name__)


@app.route("/")
def home():
   return html


@app.route('/encode', methods=['POST'])
def encode():
    if request.method == "POST":
        sentence = request.form["text"]
        sentence_encoded = encoding.garble(sentence)
        # return Response(sentence_encoded, mimetype='text/plain')
        return Response(sentence_encoded, mimetype='text/plain')


@app.route('/decode', methods=['POST'])
def decode():
    if request.method == "POST":
        encoded = request.form["encoded"]
        to_decode = encoding.decode(encoded)
    return Response(to_decode, mimetype='text/plain')




if __name__	== "__main__":
    app.run(debug=True)

