import requests
import json

file_endpt = 'https://api.gdc.cancer.gov/files/'
file_uuid = 'd853e541-f16a-4345-9f00-88e03c2dc0bc'
response = requests.get(file_endpt + file_uuid)
print json.dumps(response.json(), indent=2)

file_endpt = 'https://api.gdc.cancer.gov/files/'
file_uuid = '02b7ae7e-ec43-413b-b0f3-575b9b40973e'
response = requests.get(file_endpt + file_uuid)
print json.dumps(response.json(), indent=2)

file_endpt = 'https://api.gdc.cancer.gov/files/'
file_uuid = '004099ce-167a-4129-b29d-ce6ac54dcef7'
response = requests.get(file_endpt + file_uuid)
print json.dumps(response.json(), indent=2)
