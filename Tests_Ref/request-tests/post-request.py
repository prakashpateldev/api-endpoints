import jsonpath
import requests
import json
# import jsonpath


#API URL
url = "https://reqres.in/api/users"


def test_create_new_user():

    #Read input json file
    file = open("CreateUser.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print("User", request_json)
    #Make POST request with Json Input body
    response = requests.post(url, request_json)
    assert response.status_code == 201
    #Fetch Header from Response code
    print(response.headers.get('Content-Length'))
    print(response.headers)
    #Parse response to Json Format
    response_json = json.loads(response.text)
    #Pick Id using Json Path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

test_create_new_user()