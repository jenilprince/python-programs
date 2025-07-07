import pickle
data={"name": "JP",
      "age": 18,
      "class": "Python",
      "email": "<EMAIL>",
      "phone": 12345}
with open('app23.pkl', 'wb') as file:
    dump=pickle.dump(data, file)
    print(dump)
with open('app23.pkl', 'rb') as file:
    load=pickle.load(file)
    print(load)
