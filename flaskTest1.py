from flask import Flask, request, jsonify

app = Flask(__name__)

first_name = [{'name': 'sai'}, {'name': 'harsha'}]


@app.route('/', methods=['GET'])
def login():
    if request.method == 'GET':
        return jsonify({'message': 'hello logged in'})


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        name = {'name': request.json['name']}
        first_name.append(name)
        return jsonify({'first_name': first_name})


@app.route('/testput', methods=['PUT'])
def testput():
    if request.method == 'PUT':
        return jsonify({'put': ' put method'})


@app.route('/testdel', methods=['DELETE'])
def testdel():
    if request.method == 'DELETE':
        first_name.pop(0)
        return jsonify({'first_name': first_name})


if __name__ == '__main__':
    app.run(debug=True)
