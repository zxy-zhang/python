#将代码划分为一系列完成具体工作的函数，这样的过程成为重构
import json

def get_stored_username():
	'''如果获取了用户名，就获取它'''
	filename='username.json'
	try:
		with open(filename)as file_object:
			username=json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	'''提示输入用户名'''
	username=input("What is your name?")
	filename='username.json'
	with open(filename,'w')as file_object:
		json.dump(username,file_object)
	return username

def greet_user():
	'''问候用户，并指出其名字'''
	username=get_stored_username() 
	if username:
		print("Welcome back,"+username+" !")
	else:
		username=get_new_username()
		# username=input("What is your name?")
		# filename='username.json'
		# with open(filename)as file_object:
		# 	json.dump(username,file_object)
		print("We will remember you when you come back,"+username+" !")
		#greet_user()函数打印一条合适的消息，要么欢迎老用户回来，要么问候新用户
		#所以先调用get_stored_username()函数，只负责获取存储的用户名
		#get_new_username()负责获取并存储新的用户名
greet_user()