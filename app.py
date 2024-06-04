from flask import Flask, jsonify, render_template, request
from train import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET"])
def chat_response():
    user_input = request.args.get('msg')
    try:
        response = get_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": "error"}), 500
    

#test

@app.route("/test")
def test():
    try:
        return jsonify({"response": "working."})
    except Exception as e:
        return jsonify({"response": "error."}), 500

if __name__ == '__main__':
    app.run()
