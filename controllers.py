from app import *

input_file = open ("api_structure.json")
operations = json.load(input_file)

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