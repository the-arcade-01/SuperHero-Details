import requests
import json
import matplotlib.pyplot as plt

access_token = '503983410507122'
name = 'batman'
base_url = f'https://superheroapi.com/api/{access_token}/search/{name}'

r = requests.get(base_url)
data = r.json()
results = data['results'][0]
print(results.keys())
dict_powerstats = {}
for item in results['powerstats']:
    dict_powerstats[item] = int(results['powerstats'][item])
# print(dict_powerstats)
print(type(results['image']))
# print(results['powerstats'])
# print(results['biography'])
# print(results['appearance'])
# print(results['work'])
# print(results['connections'])
# print(results['image'])
