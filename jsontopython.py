import json

#some json
x = '{"name":"Jon", "age":30, "city":"New York"}'

#parse x
y = json.loads(x)

#result
print(y["city"])