import requests

key = ""
output = "json"
lat = "25.1212837"
lon = "121.5282113"
radius = "1500"
keyword = "刀削麵"

url_nearby_search = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{output}?location={lat}%2C{lon}&radius={radius}&keyword={keyword}&type=restaurant&key={key}"

payload={}
headers = {}

response = requests.request("GET", url_nearby_search, headers=headers, data=payload)

print(response.text)