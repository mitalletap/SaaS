from app import *
# export FLASK_ENV=development

input_file = open ("api_structure.json")
operations = json.load(input_file)

# @app.route('/')
# def index():
#     return jsonify('ADD SOMETHING')

# All Shit
@app.route('/operations')
def allOperations():
    return jsonify(operations)     

# Correct way to pass arguments through JSON Data and URL
# What The Shit
@app.route('/what-the-shit')
def whatTheShit():
    post_response = operations[0]["name"].format(request.args.get("name"))
    new_operations = [post_response, operations[0]["data"]]
    return jsonify(new_operations) 

# What Is This Shit

@app.route('/what-is-this-shit')
def whatIsThisShit():
    post_response = operations[1]["name"]
    new_operations = [post_response, operations[1]["data"]]
    return jsonify(new_operations) 
    
# How Do I Use This Shit
@app.route('/how-do-i-use')
def howDoIUseThisShit():
    post_response = operations[2]["name"]
    new_operations = [post_response, operations[2]["data"]]
    return jsonify(new_operations) 


# Can You Believe This Shit
@app.route('/can-you-believe')
def canYouBelieve():
    post_response = operations[3]["name"]
    new_operations = [post_response, operations[3]["data"]]
    return jsonify(new_operations) 


# How Do You Test This Shit
@app.route('/how-do-you-test')
def howDoYouTest():
    post_response = operations[4]["name"]
    new_operations = [post_response, operations[4]["data"]]
    return jsonify(new_operations) 

# Ive Got Shit To Do
@app.route('/shit-to-do')
def shitToDo():
    post_response = operations[5]["name"]
    new_operations = [post_response, operations[5]["data"]]
    return jsonify(new_operations) 

# Same Shit Different 
@app.route('/same-shit')
def sameShit():
    post_response = operations[6]["name"]
    new_operations = [post_response, operations[6]["data"]]
    return jsonify(new_operations) 

# Looks Like Shit
@app.route('/look-like')
def looksLikeSHIT():
    post_response = operations[7]["name"]
    new_operations = [post_response, operations[7]["data"]]
    return jsonify(new_operations) 

# Stop Talking Shit
@app.route('/stop-talking')
def stopTalking():
    post_response = operations[8]["name"]
    new_operations = [post_response, operations[8]["data"]]
    return jsonify(new_operations) 

# You Have Alot Of Shit
@app.route('/alot-of')
def alotOf():
    post_response = operations[8]["name"].format(request.args.get("name"))
    new_operations = [post_response, operations[8]["data"]]
    return jsonify(new_operations) 







@app.route('/operations')
def operation():
    return jsonify(operations)


