users={
    "id": "1",
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])

print(users)
print(type(users))
print(f"\nubah dict ke json")
import json
result = json.dumps(users)  # dumps: mengubah ke json (string)
print(type(result))
print(result)

with open('result.json', 'w') as file:  # membuat/menulis file result.json
    json.dump(users, file)