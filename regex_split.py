import re

str = "The rain in spain"
x = re.split("\s", str)
print(x)

str = "The rain in spain"
x = re.split("\s", str, 1)
print(x)

