import re

str = "The rain in Spain falls mainly in the plain!"

x = re.findall("aix*", str)

print(x)

if (x):
	print("Yes, it's match")
else:
	print("No match")

x = re.findall("ain+", str)

print(x)

if (x):
	print("Yes, it's match")
else:
	print("No match")

x = re.findall("aix+", str)

print(x)

if (x):
	print("Yes, it's match")
else:
	print("No match")