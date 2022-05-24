#generate and save a json file from code below
import json

data = {
      "description": 'This is an example #1',
      "name": 'NFT Example #1',
      "attributes": [
        {
          "trait_type": 'color',
          "value": 'red'
        }
      ],
      "image": 'https://ipfs.io/ipfs/QmReweQey8JiwiTG7iJuW9Vzp5GncKLEApXqMYYsbk1Eff',
    }

json_str = json.dumps(data)

print(json.dumps(data, indent=4))

with open('data.json', 'w') as f:
    json.dump(data, f)