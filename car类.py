class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0


	def get_descriptive_name(self):
		'''返回简洁的描述信息'''
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it")


	def updata_odometer(self,mileage):

		'''将里程表读数设置为指定的值
		   禁止将里程数回调'''
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		self.odometer_reading +=miles
		'''将里程表增加指定的量'''
      
		

my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.updata_odometer(23599)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.updata_odometer(10)
'''通过方法修改属性的值'''
#my_new_car.odometer_reading=23
#直接修改属性的值
my_new_car.read_odometer()

