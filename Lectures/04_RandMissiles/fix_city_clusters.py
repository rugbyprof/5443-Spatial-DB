import json

with open("cities.json") as f:
    # data = f.read()
    data = json.load(f)

# print(data)

for i in range(len(data["features"])):
    if data["features"][i]["geometry"]["type"] == "MultiPoint":
        data["features"][i]["geometry"]["type"] = "Polygon"
        data["features"][i]["geometry"]["coordinates"] = [
            data["features"][i]["geometry"]["coordinates"]
        ]
        data["features"][i]["geometry"]["coordinates"][0].append(
            data["features"][i]["geometry"]["coordinates"][0][0]
        )

print(data)

with open("cities_fixed.json", "w") as f:
    f.write(json.dumps(data, indent=2))
