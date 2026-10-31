
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask API!"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello World!"})

@app.route('/about')
def about():
    return jsonify({"project": "Flask API using Docker and Kubernetes"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# Testing automatic Jenkins trigger