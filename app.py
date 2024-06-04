# from flask import Flask, jsonify, render_template, request
# from train import get_response
# import logging

# app = Flask(__name__)
# logging.basicConfig(level=logging.DEBUG)



# @app.route("/")
# def index():
#     return render_template('index.html')


# @app.route("/get", methods=["GET", "POST"])

# def chat_response():
#     user_input = request.args.get('msg')
#     response = get_response(user_input)
#     return jsonify({"response": response})


# if __name__ == '__main__':
#     app.run(port=8000, debug=True)

from flask import Flask, jsonify, render_template, request
from train import get_response
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET"])
def chat_response():
    user_input = request.args.get('msg')
    app.logger.debug(f"Received message: {user_input}")
    try:
        response = get_response(user_input)
        app.logger.debug(f"Response: {response}")
        return jsonify({"response": response})
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"response": "Sorry, there was an error processing your request."}), 500

@app.route("/test")
def test():
    try:
        return jsonify({"response": "Test route is working."})
    except Exception as e:
        app.logger.error(f"Test route error: {str(e)}")
        return jsonify({"response": "Error in test route."}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)
