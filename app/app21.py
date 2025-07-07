import json
data={"name": "JP",
      "age": 18,
      "class": "Python",
      "email": "<EMAIL>",
      "phone": 12345}
with open('app21.json', 'w') as file:
    add=json.dump(data, file)
    print(add)
with open('app21.json', 'r') as file:
    show=json.load(file)
    print(show)