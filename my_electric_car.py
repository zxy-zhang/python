from car import ElectricCar
my_tesla=ElectricCar('tesla','model',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#从一个模块存储多个类