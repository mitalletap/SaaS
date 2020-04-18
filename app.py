from flask import Flask
from flask import jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return jsonify('ADD SOMETHING')


@app.route('/hello')
def hello():
    return jsonify('Hello')