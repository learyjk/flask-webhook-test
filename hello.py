from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
