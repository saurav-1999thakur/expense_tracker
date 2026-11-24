from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "Pinging the server...."

@app.route('/api/summery')
def summery():
    return jsonify({'amount': 3000, 'currency': "INR"})

@app.route('/not-found')
def not_found():
    return "Page not found", 404