from app import *
# export FLASK_ENV=development

input_file = open ("api_structure.json")
operations = json.load(input_file)

@app.route('/')
def index():
    return jsonify('ADD SOMETHING')

# Correct way to pass arguments through JSON Data and URL
@app.route('/what')
def hello():
    post_name = request.args.get("name")
    return jsonify(operations[0]["name"].format(post_name)) 


@app.route('/operations')
def operation():
    return jsonify(operations)