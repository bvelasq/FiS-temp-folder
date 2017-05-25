import urllib
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'lhr'
url = main_api + urllib.urlencode({'address': address})
# urllib.parse.urlencode changed to urllib.urlencode as the former function is python 3.x exclusive
print(url)

json_data = requests.get(url).json()
json_status = json_data['status']
print('API Status: ' + json_status)

formatted_address = json_data['results'][0]['formatted_address']
print()
print(formatted_address)
~                                                                                                       
