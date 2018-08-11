from car import Car 

class Battery():
	'''模拟汽车电瓶'''
	def __init__(self,battery_size=70):
		'''初始化电瓶属性'''
		self.battery_size=battery_size

	def describe_battery(self):
		'''打印一条描述电瓶容量的消息'''
		print("This car has a "+str(self.battery_size)+"-KWH battery.")


	def get_range(self):
		'''打印一条消息，指出电瓶的续航里程'''
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=170
		message="This car can go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)



class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()


	def __init__(self,make,model,year):
		'''初始化父类属性，再初始化电动汽车特有属性'''
		super().__init__(make,model,year)
		self.battery=Battery()