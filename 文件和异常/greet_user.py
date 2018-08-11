import json

filename='username.json'

with open(filename)as file_object:
	username=json.load(file_object)
	#使用json.load()将存储在username.json中的信息读取到bianliangusername中
	print("Welcome back "+username+" !")
