import requests
import json

key = ""
output = "json"
place_id = "ChIJ2VpInIeuQjQRQfGwrU7Aj7U" # 一品刀削麵的id
language = "zh-TW"

url_place_details = f"https://maps.googleapis.com/maps/api/place/details/{output}?key={key}&place_id={place_id}&language={language}"

payload={}
headers = {}

response = requests.request("GET", url_place_details, headers=headers, data=payload).json()
reviews = response['result']['reviews']
print(reviews)

with open('reviews.json', 'w', encoding='utf8') as f:
    json.dump(reviews, f, ensure_ascii=False)