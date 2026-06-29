import json

json_string = '{"name": "John", "age": 30, "city": "New York", "id": [{"id":1}]}'

data = json.loads(json_string)
print(type(data))
print(data)
print(json.dumps(data))
print(json.dumps("{'name': 'John', 'age': 30, 'city': 'New York'}"))

with open('example.json', 'w') as file:
    json.dump(data, file, indent=4)


