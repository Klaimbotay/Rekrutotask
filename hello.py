from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def helloRekruto():
    name = request.args.get('name', '')
    message = request.args.get('message', '')
    return f'Hello {name}!<br>{message}'