#创建类
class Dog():

	def __init__(self,name,age):
		
		self.name=name
		self.age=age
		
	def sit(self):
		print(self.name.title()+" is now sitting.")


	def roll_over(self):
			print(self.name.title()+" rolled over.")

my_dog = zDog('kaochuan',1)
your_dog=Dog('Lucy',2)
my_dog.sit()
my_dog.roll_over()

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old")

print("\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old")
your_dog.sit()
your_dog.roll_over()