# Object Oriented Programming in Python

class Dog:
	def bark(self):
		print("bark")

	def add_one(self, x):
		return x+1

d = Dog()
print(type(d))
print(d.add_one(5))