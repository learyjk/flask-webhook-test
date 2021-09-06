from flask import Flask, request, Response, send_from_directory, abort

application = Flask(__name__)

@application.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@application.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)


@application.route("/nft/<path:file_name>")
def get_file(file_name):
    print(file_name)
    return "Thanks."

if __name__ == "__main__":
    application.run(host='0.0.0.0')
