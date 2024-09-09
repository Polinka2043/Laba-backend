from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        text = request.json['text']
        with open('data.txt', 'a') as f:
            f.write(text + '\n')
        return jsonify({'message': 'Data received'})
    elif request.method == 'GET':
        with open('data.txt', 'r') as f:
            data = f.read()
        return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True, port=5001)