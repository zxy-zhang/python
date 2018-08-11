#传递列表
#将一个名字列表传递给greet_users()函数中，函数问候列表的每个人
def greet_users(names):
	for name in names:
		msg="Hello,"+name.title()+"!"
		print(msg)
usernames=['aa','bb','cc']
#定义了一个用户列表usernames,然后调用greet_users()
greet_users(usernames)


#在函数中修改列表
#首先创建一个列表，包含要打印的设计
unprinted_designs=['iphone case','robot pendant','dodecahedroon']
completed_models=[]
#创建一个空列表，将每个打印设计都转移到这个列表中
while unprinted_designs:
	current_design=unprinted_designs.pop()
	#从末尾删除一个设计，将其存储到current_design中
	print("Printing model: "+current_design)
	completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)


def print_models(unprinted_designs,completed_models):
	#定义了两个形参，一个需要打印的设计列表，一个打印好的模型列表
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		print("Printinng model: "+current_design)
		completed_models.append(current_design)
		#将设计逐个从未打印的设计列表中取出，并加入到打印好的模型列表
def show_completed_models(completed_models):
	#定义函数show_completed_models,包含一个形参：打印好的模型列表
	print("\nThe folliwing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecaheedron']
completed_models=[]
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)



#禁止函数修改列表，比如有一个未打印的列表，并编写了一个将这些设计打印好的模型列表的函数
#想打印所有设计，也想保留原来未打印的设计列表
#为了实现这个想法，可想函数传递列表的是副本而不是原件
#function_name(list_name[:])
#切片表示法[:]创建列表的副本
#可以这么调用函数
#print_models(unprinted_designs[:],completed_models)