from app import *
# export FLASK_ENV=development

#blueprint makes it all have a similar api route, may not seem like much but it will help out a ton in the future
#especially if you have a large project
mod = Blueprint('api', __name__,)
input_file = open("backend/api_structure.json")
operations = json.load(input_file)

@app.route('/')
def index():
    return jsonify('I BROKE IT ')

# All Shit
@mod.route('/operations')
def allOperations():
    return jsonify(operations)     

# Correct way to pass arguments through JSON Data and URL
# What The Shit
@mod.route('/what-the-shit')
def whatTheShit():
    post_response = operations[0]["name"].format(request.args.get("name"))
    new_operations = [post_response, operations[0]["data"]]
    return jsonify(new_operations) 

# What Is This Shit

@mod.route('/what-is-this-shit')
def whatIsThisShit():
    post_response = operations[1]["name"]
    new_operations = [post_response, operations[1]["data"]]
    return jsonify(new_operations) 
    
# How Do I Use This Shit
@mod.route('/how-do-i-use')
def howDoIUseThisShit():
    post_response = operations[2]["name"]
    new_operations = [post_response, operations[2]["data"]]
    return jsonify(new_operations) 


# Can You Believe This Shit
@mod.route('/can-you-believe')
def canYouBelieve():
    post_response = operations[3]["name"]
    new_operations = [post_response, operations[3]["data"]]
    return jsonify(new_operations) 


# How Do You Test This Shit
@mod.route('/how-do-you-test')
def howDoYouTest():
    post_response = operations[4]["name"]
    new_operations = [post_response, operations[4]["data"]]
    return jsonify(new_operations) 

# Ive Got Shit To Do
@mod.route('/shit-to-do')
def shitToDo():
    post_response = operations[5]["name"]
    new_operations = [post_response, operations[5]["data"]]
    return jsonify(new_operations) 

# Same Shit Different 
@mod.route('/same-shit')
def sameShit():
    post_response = operations[6]["name"]
    new_operations = [post_response, operations[6]["data"]]
    return jsonify(new_operations) 

# Looks Like Shit
@mod.route('/look-like')
def looksLikeSHIT():
    post_response = operations[7]["name"]
    new_operations = [post_response, operations[7]["data"]]
    return jsonify(new_operations) 

# Stop Talking Shit // also added the args
@mod.route('/stop-talking')
def stopTalking():
    post_response = operations[8]["name"]
    response = request.args.get('name')
    new_operations = [post_response.format(response), operations[8]["data"]]
    return jsonify(new_operations) 

# You Have Alot Of Shit
@mod.route('/alot-of')
def alotOf():
    post_response = operations[8]["name"].format(request.args.get("name"))
    new_operations = [post_response, operations[8]["data"]]
    return jsonify(new_operations) 




@mod.route('/operations')
def operation():
    return jsonify(operations)

#returns controller.Endpointcontrollers
#@mod.route('/name')
#def name():
#    return jsonify(__name__)