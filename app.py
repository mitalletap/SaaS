from flask import Flask
from flask import request
from flask import jsonify

app=Flask(__name__)

operations = [{"name":"Who the fuck are you anyway","url":"/anyway/:company/:from","fields":[{"name":"Company","field":"company"},{"name":"From","field":"from"}]}]




@app.route('/')
def index():
    return jsonify('ADD SOMETHING')


@app.route('/hello')
def hello():
    post_id = request.args.get('id')
    return jsonify(post_id)


@app.route('/operations')
def operation():
    return jsonify(operations)
