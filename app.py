from flask import Flask, jsonify, render_template, request
from train import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])

def chat_response():
    user_input = request.args.get('msg')
    response = get_response(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(port=8000, debug=True)