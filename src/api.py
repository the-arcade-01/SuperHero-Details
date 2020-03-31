import requests
import json

access_token = '503983410507122'
name = 'superman'
base_url = f'https://superheroapi.com/api/{access_token}/search/{name}'

r = requests.get(base_url)
data = r.json()
results = data['results'][0]
print(results.keys())
print(results['name'])
# print(results['powerstats'])
# print(results['biography'])
# print(results['appearance'])
# print(results['work'])
# print(results['connections'])
# print(results['image'])
