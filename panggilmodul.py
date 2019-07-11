import mymodule

x = dir(mymodule)
print(x)

mymodule.greeting("Elga Purwacaraka")

a = mymodule.person1['name']
print (a)

for x in (mymodule.person1):
	print (x, mymodule.person1[x])


for x,y in mymodule.person1.items():
	print (x, y)



	