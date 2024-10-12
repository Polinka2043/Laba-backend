from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/api/data', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
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
            with open('data.txt', 'r') as f:
                data = f.read()
            return jsonify({'data': data})
        except IOError as e:
            return jsonify({'error333': {'message': str(e), 'code': 500}}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)