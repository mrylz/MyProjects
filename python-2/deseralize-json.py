import json
with open("product.json") as file:
    data = json.load(file)
print(data["title"])    
print(data["color"])
print(data["rating"])