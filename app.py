from flask import Flask
from flask import request
from flask import jsonify

app=Flask(__name__)

@app.route('/')
def index():
    return jsonify('ADD SOMETHING')


@app.route('/hello')
def hello():
    post_id = request.args.get('id')
    return jsonify(post_id)

