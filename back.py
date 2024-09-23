from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_text():
    text = request.form['text']
    with open('data.txt', 'a') as f:
        f.write(text + '\n')
    return 'Text received!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)