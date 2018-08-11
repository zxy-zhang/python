# 8-12 三明治 ： 编写一个函数， 它接受顾客要在三明治中添加的一系列食材。 这个函数只有一个形参（它收集函数调用中提供的所有食材） ，   
# 并打印一条消息， 对顾客点的三明治进行概述。 调用这个函数三次， 每次都提供不同数量的实参。  
def sand_make(*ingredients):
	print('添加的食材有：')
	for i in ingredients:
		print('--'+i)
sand_make('1','2','3','4')
sand_make('3')
sand_make('2','4')

# 8-13 用户简介 ： 复制前面的程序user_profile.py， 在其中调用build_profile() 来创建有关你的简介；   
# 调用这个函数时， 指定你的名和姓， 以及三个描述你的键-值对。 
def user_profile(first,last,**user_info):
	name_file={}
	name_file['first_name']=first
	name_file['last_name']=last
	for key,value in user_info.items():
		name_file[key]=value
	return name_file
user_a=user_profile('ma','yun',company='TaoBao',Sex='man')
print(user_a)
user_b=user_profile('1','2',Sex='man')
print(user_b)

# 8-14 汽车 ： 编写一个函数， 将一辆汽车的信息存储在一个字典中。 这个函数总是接受制造商和型号， 还接受任意数量的关键字实参。   
# 这样调用这个函数： 提供必不可少的信息， 以及两个名称—值对， 如颜色和选装配件。 这个函数必须能够像下面这样进行调用：  
# car = make_car('subaru', 'outback', color='blue', tow_package=True)  
# 打印返回的字典， 确认正确地处理了所有的信息。
def car_msg(manufacturer,model,**else_info):
	bas_msg={}
	bas_msg['manufacturer']=manufacturer
	bas_msg['model']=model
	for key,value in else_info.items():
		bas_msg[key]=value
	return bas_msg
car=car_msg('subaru','outback',color='blue',tow_package=True)
print(car)