from flask import Flask, request, jsonify
from flask_cors import CORS

# Set up Flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/test', methods=['GET'])
def predict_digit():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
