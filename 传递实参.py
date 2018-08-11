def describe_pet(animal_type,pet_name):
	#函数调用中的每个市残念都关联到函数定义中的一个形参，最坚实单的是基于实参的顺序，这种关联方式是位置实参
	#位置实参的顺序很重要
	print("\nI have a "+animal_type)
	print("My "+animal_type+" name is "+pet_name.title()+".")
describe_pet('dog','barcbuce')
describe_pet('cat','ll')  
#多次调用函数

def describe_pet(pet_name,animal_type='dog'):   #默认值
	print("\nI have a "+animal_type+".")
	print("\nMy "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='kaochuan')


def describe_pet(pet_name='kaochuan',animal_type='dog'):   
#在使用默认值的时候，在形参列表必须先列出没有默认值的形参，再列出有默认值的形参，能正确解读位置形参
	print("\nI have a "+animal_type+".")
	print("\nMy "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet()

#用于存储国家的形参指定默认值，三个城市有一个不属于默认值的国家
def describe_city(name,country='China'):         
	print(name.title()+" is in "+country.title()+".")
describe_city('Beijing')
describe_city('shanghai')
describe_city('New york','American')