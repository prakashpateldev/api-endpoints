import jsonpath
import requests
import json


#API URL
url = "https://reqres.in/api/users"


def test_create_new_user_now():

    #Read input json file
    file = open("/CreateUser.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print("User", request_json)
    response = requests.post(url, request_json)
    assert response.status_code == 201

def test_create_other_user_now():

    #Read input json file
    file = open("/home/parkash/Documents/API Automation/CreateUser.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print("User", request_json)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    print(response.headers.get('Content-Length'))
    print(response.headers)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
