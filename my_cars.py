from car import Car
from electric_car import ElectricCar

my_beetle=Car('volkswage','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())


#从一个模块导入多个类