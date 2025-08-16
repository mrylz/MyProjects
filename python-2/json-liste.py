data = [
    {
        "id" : 1,
        "title" : "Macbook Pro",
        "price" : 9000,
        "category" : "bilgisayar"
    },
    {
        "id" : 2,
        "title" : "Macbook Air",
        "price" : 7000,
        "category" : "bilgisayar"
    }
]
import json
with open("product2.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)