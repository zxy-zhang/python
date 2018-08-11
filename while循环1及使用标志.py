'''
current_number=1
while current_number<=5:
	print(current_number)
	current_number+=1

prompt="\nTell me something,and I will repeat it back to you:"    #让用户选择何时退出
prompt+="\nEnter 'quit' to end the program: "
message=""             #创建一个变量message，用于存储用户的值
while message!='quit':
	message=input(prompt)
	if message!='quit':           #在消息不是退出值才打印
		print(message)
'''	
prompt="\nTell me something,and I will repeat it back to you:"    #让用户选择何时退出
prompt+="\nEnter 'quit' to end the program: "
active=True
while active:
	message=input(prompt)
	if message=='quit':
		active=False
	else:
		print(message)