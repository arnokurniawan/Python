import json

#python object(dict)
z = {
	"name" : "Jhon",
	"age" : 30,
	"city" : "New York"
}

#convert into json
y = json.dumps(z)

#the resul is a json string
print(y)


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))