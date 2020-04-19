from app import *
from flask import Blueprint
#blueprint makes it all have a similar api route, may not seem like much but it will help out a ton in the future
#especially if you have a large project
mod = Blueprint('api', __name__,)
input_file = open ("api_structure.json")
operations = json.load(input_file)


@mod.route('/')
def index():
    return jsonify('ADD SOMETHING')


@mod.route('/hello', methods=['POST','GET'])
def hello():
    post_name = request.args.get('name')
    return jsonify(operations[0]["name"].format(post_name))


@mod.route('/operations')
def operation():
    return jsonify(operations)
    
#module name
@mod.route('/name')
def name():
    return __name__