import requests
import json
import jsonpath




def test_Add_new_data():
    App_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("/CreateUser.json", "r")
    json_input = json.loads(file.read())
    response = requests.post(App_URL, json_input)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "http://thetestingworldapi.com/Api/technicalskills"
    file = open("/home/parkash/Documents/API Automation/TechDetails.json", "r")
    json_input = json.loads(file.read())
    json_input['id'] = int(id[0])
    json_input['st_id'] = id[0]
    response = requests.post(tech_api_url,json_input)
    print(response.text)

    add_api_url = "http://thetestingworldapi.com/api/addresses"
    file = open("/home/parkash/Documents/API Automation/address.json", "r")
    json_input = json.loads(file.read())
    json_input['stId'] = id[0]
    response = requests.post(add_api_url,json_input)
    #print(response.text)


    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/"+ str(id[0])
    response = requests.get(final_details)
    print(response.text)



