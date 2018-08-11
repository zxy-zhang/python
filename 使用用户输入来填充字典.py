responses={}          
#设置一个标志(polling_active),支出调查是否继续
polling_active=True
while polling_active:
	#提示输入被调查者的名字和回答
	name=input("\nWhat's your name?")
	response=input("which mountain would you like to climb someday?")
	#提示用户输入姓名及其喜欢爬哪座山
	responses[name]=response   #将response值关联到字典responses值中的name上
	#将这些信息存储在字典responses中
	repeat=input(" would you like another person respond?(yes/no)")
	#询问用户调查是否继续
	if repeat=='no':
		polling_active=False
print("\n--- poll result ---")
for name,response in responses.items():
	print(name+",Would you like to climb "+response+".")