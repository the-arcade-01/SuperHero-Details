import requests
import json
import matplotlib.pyplot as plt

access_token = '503983410507122'
name = 'harry potter'
base_url = f'https://superheroapi.com/api/{access_token}/search/{name}'

r = requests.get(base_url)
data = r.json()
results = data['results'][0]
print(results.keys())
dict_powerstats = {}
for item in results['powerstats']:
    dict_powerstats[item] = int(results['powerstats'][item])
biography = results['biography']
# print(biography)
# print(type(biography))
print(dict_powerstats)
# print(dict_powerstats)
# print(results['powerstats'])
# print(results['biography'])
# print(results['appearance'])
# print(results['work'])
# print(results['image'])
