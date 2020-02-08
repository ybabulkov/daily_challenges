from urllib import request
import json

searchesPercentage = []
response = request.urlopen("https://insights.stackoverflow.com/trends/get-data")
payload = response.read()
print(type(payload))
stackoverflow_trends = json.loads(payload)
print(type(stackoverflow_trends))
tagDict = stackoverflow_trends["TagPercents"]

for key in tagDict.keys():
    if "python" in key:
        print(key, "-", tagDict[key][-1])

