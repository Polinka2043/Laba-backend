from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def read_data():
    user_input = request.get_json()['userInput']
    with open('data.txt', 'r') as f:
        data = f.read()
    return jsonify({'result': data})

if __name__ == '__main__':
    app.run(debug=True)