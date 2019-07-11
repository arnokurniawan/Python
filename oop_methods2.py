class Hero:
	age = 10
	def __init__(self, name):
		self.name = name
		self.address = "Mampang"

	def nama(self):
		print("alamat ku :" + self.name)

	def alamat(self):
		print("alamat ku :" + self.address)


hero = Hero('sniper')

hero.alamat()
umur = hero.age
print (umur)