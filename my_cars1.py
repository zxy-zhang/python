import car


my_beetle=car.Car('volkswage','beetle',2016)
#用语法module_name.class_name访问需要的类
#创建甲壳虫的汽车
print(my_beetle.get_descriptive_name())

my_tesla=car.ElectricCar('tesla','roadster',2016)
#创建特斯拉Roadster的汽车
print(my_tesla.get_descriptive_name())


#导入整个模块