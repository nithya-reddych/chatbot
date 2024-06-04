from flask import Flask, jsonify, render_template, request
from train import get_response
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])

def chat_response():
    user_input = request.args.get('msg')

    #debug
    app.logger.debug(f"Received message: {user_input}")
    response = get_response(user_input)
    app.logger.debug(f"Response: {response}")


    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
