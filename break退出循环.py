prompt="\nTell me something,and I will repeat it back to you:"    #让用户选择何时退出
prompt+="\nEnter 'quit' to end the program: "
while True:
	city=input(prompt)
	if city=='quit':
		break                   #任何python循环都可以使用break语句来退出遍历列表或字典的for循环
	else:
		print("I'd love to go to "+city.title()+"!")