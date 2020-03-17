from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return jsonify({'message': 'hello logged in'})


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        return jsonify({"hello": "sai"})


if __name__ == '__main__':
    app.run(debug=True)
