from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Welcome to the backend!</h1>'

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return '', 404

@app.route('/api/data', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        # Same as before
        if request.headers['Content-Type'] != 'application/json':
            return jsonify({'error123': {'message': 'Invalid content type', 'code': 415}}), 415
        data = request.get_json()
        user_input = data.get('userInput')
        if user_input is None:
            return jsonify({'error321': {'message': 'Missing userInput', 'code': 400}}), 400
        try:
            with open('data.txt', 'a') as f:
                f.write(user_input + '\n')
            return jsonify({'data': 'Data received'})
        except IOError as e:
            return jsonify({'error000': {'message': str(e), 'code': 500}}), 500
    elif request.method == 'GET':
        try:
            with open('data.txt', 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    return jsonify({'data': last_line})
                else:
                    return jsonify({'data': 'No data available'})
        except IOError as e:
            return jsonify({'error333': {'message': str(e), 'code': 500}}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
