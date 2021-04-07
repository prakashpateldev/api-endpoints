import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Create some test data for our catalog in the form of a list of dictionaries.

accounts = [
    {'id': 0,
     'name': 'Prakash Patel',
     'address': '71 oxhey lane, ha5 4ay',
     'balance': 10},
    {'id': 1,
     'name': 'Aarav Patel',
     'address': '73 oxhey lane, ha5 4ay',
     'balance': 20},
    {'id': 2,
     'name': 'XYZ',
     'address': '75 oxhey lane, ha5 4ay',
     'balance': 30}
]
@app.route('/api/v1/resources/accounts/all', methods=['GET'])
def api_all():
    return jsonify(accounts)

#app.run()

@app.route('/api/v1/resources/accounts', methods=['GET'])
def api_id():
    #Check if ID was provided as part of URL.
    #If ID is provided, assign it to a variable.
    #if no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #Create an empty list for our results
    results = []
    #print(id)
    for account in accounts:
        if account['id'] == id:
            results.append(account)
    return jsonify(results)
app.run()


