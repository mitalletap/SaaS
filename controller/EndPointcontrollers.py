from app import *
# export FLASK_ENV=development

input_file = open ("api_structure.json")
operations = json.load(input_file)

@app.route('/')
def index():
    return jsonify('ADD SOMETHING')

# Correct way to pass arguments through JSON Data and URL
@app.route('/what-the-shit')
def whatTheSHIT():
    post_response = operations[0]["name"].format(request.args.get("name"))
    new_operations = [post_response, operations[0]["data"]]
    return jsonify(new_operations) 

@app.route('/what-is-this-shit')
def whatIsThisSHIT():
    post_response = operations[1]["name"]
    new_operations = [post_response, operations[1]["data"]]
    return jsonify(new_operations) 
    

@app.route('/how-do-i-use')
def howDoIUseThisSHIT():
    post_response = operations[2]["name"]
    new_operations = [post_response, operations[2]["data"]]
    return jsonify(new_operations) 

@app.route('/operations')
def operation():
    return jsonify(operations)


