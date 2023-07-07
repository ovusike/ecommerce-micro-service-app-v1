import logging
from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    app.logger.info("Signup process started with the inputs: %s", data)
    username = data.get('username')
    password = data.get('password')
    app.logger.info("UserName: %s", username)
    app.logger.info("Password: %s", password)
    return 'User created', 201

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    app.logger.info("Signin process started with the inputs: %s", data)
    username = data.get('username')
    password = data.get('password')
    app.logger.info("UserName: %s", username)
    app.logger.info("Password: %s", password)
    return 'Logged in successfully', 200

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000)
