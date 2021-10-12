import json

dict1 = '{ "name":"John", "age":30, "city":"New York"}'

a=json.loads(dict1)
print(a['age'])


