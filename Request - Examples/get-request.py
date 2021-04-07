import requests
import json
import jsonpath


url = "https://reqres.in/api/users?page=2"

#Send data Requests
response = requests.get(url)
print(response)

#Display Response Content
#print(response.content)
#print(response.headers)


#Parse response to Json format
json_response = json.loads((response.text))
print(json_response)

#Fetch value using json_path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print("Number of pages", pages)
assert pages[0] == 2