#传递任意数量的实参
def make_pizza(*toppings):
	#创建一个名为toppings的空元祖
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#python将实参封装到一个元组中，即使函数只收到一个值

#将print()语句替换为一个循环，对配料表进行遍历，对顾客点的pizza进行描述
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for topping in toppings:
		print("-"+topping)
make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms','green pepper','extra cheese')

#使用任意数量关键字的实参
#函数build_profile()接受名和姓，同时还接受任意数量的关键字实参
def build_profile(first,last,**user_info):
	#创建一个空字典user_info
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
	#遍历user_info中的键-值对，并将每个键值对和加入到字典profile中
user_profile=build_profile('albert','einstein',location='prinction',field='physics')
#调用bui_profile(),向他传递名和姓以及两个键值对，并将返回的profile存储在变量user_profile中
print(user_profile)