
class Person:
	def __init__(self,nama,alamat,umur):  
		self.name = nama
		self.address = alamat
		self.age = umur

	def say_hi(self):
		print('Hello, my name is {} \n my adress is {} \n my age  {}'. \
			format(self.name,self.address, self.age)
			)
		


p = Person('Swaroop','Mampang, Jaksel', 28)
p.say_hi()

p.name = 'Solihin'
p.address = 'Bandung'
p.say_hi()

del p.name
del p.age
print(p.__dict__)

p2 = Person('Ali','Bandung', 25)
p2.say_hi()



#p = Person()
#p.say_hi()

