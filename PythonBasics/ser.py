import requests
import json

response =requests.get("https://reqres.in"+"/api/users?page=2")
print(json.dumps(response.json()))
