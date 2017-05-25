
import requests
import urllib

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = 'lhr'
url = main_api + urllib.urlencode({'address': address})
# urllib.parse.urlencode changed to urllib.urlencode as the former function is python 3.x
json_data = requests.get(url).json()
print(json_data)

