from flask import Flask, request,redirect, url_for
app = Flask(__name__)

@app.route('/', methods =['GET'])
def hello():
    if request.method == 'GET':
        return "hello"

@app.route('/admin')
def admin():
    return 'hello admin'

@app.route('/login/<name>')
def login_guest(name):
    return f'hello guest user {name}'

@app.route('/user/<name>')
def user(name):
    if name != 'admin':
        redirect(url_for('login_guest'))
    else:
        redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
