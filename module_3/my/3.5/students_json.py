import json


studens_1 = {
    "first_name": "Greg",
    "fast_name": "Dean",
    "certificate": True,
    "scores": [70, 80, 90],
    "description": "Good job, Greg"
  }
studens_2 = {
   "first_name": "Wirt",
    "fast_name": "Wood",
    "certificate": True,
    "scores": [70, 80.2, 90],
    "description": "Nicelly done"
  }

#Data = [studens_1, studens_2]

#data_json = json.dumps(Data, indent=4, sort_keys=True)
#data_again = json.loads(data_json)
#print(sum(data_again[0]["scores"]))

#print(json.dumps(Data, indent=4, sort_keys=True))

#with open("st.json", "w") as f:
#   json.dump(Data, f, indent=4, sort_keys=True)

with open("st.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))
