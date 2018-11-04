import json
import requests

headers = {
    'AccountKey': 'BOiwSe71Tl2YyOlRITpMyw==',
    'accept': 'application/json'
}

arr = []
uri = 'http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip='

for i in range(0, 26500, 500):
    response = requests.get(uri + str(i), headers=headers)
    jsonObj = json.loads(response.content)
    arr += jsonObj['value']

print(len(arr))
with open("bus_routes.json", "w") as outfile:
    json.dump(arr, outfile, sort_keys=True, indent=4)