def get_formatted_name(first_name,last_name):
 	full_name=first_name+' '+last_name
 	return full_name.title()
muician=get_formatted_name('jimi','hendrix')      
#提供一个变量，用于存储返回的值（这里返回值存储在muicain中）
print(muician)

def get_formatted_name(first_name,middle_name,last_name):
    full_name=first_name+' '+middle_name+' '+last_name
    return full_name.title()
muician=get_formatted_name('john','lee','hooker')    
#只要提供名，中间名，姓，在适当的地方加上空格，将结果转换为首字母大写模式，就可以输出一个人的名字   
print(muician)

#适用于由中间名和没有中间名的，让实参变为可选的
def get_formatted_name(first_name,last_name,middle_name=''):
	if middle_name:
		full_name=first_name+' '+middle_name+' '+last_name
	else:
		full_name=first_name+' '+last_name
	return full_name.title()
muician=get_formatted_name('john','lee','hooker')    
print(muician)
muician=get_formatted_name('jimi','hendrix')
print(muician)


#返回字典
def build_person(first_name,last_name):
	person={'first':first_name,'last':last_name}
	return person
muician=build_person('jimi','hendrix')
print(muician)


def build_person(first_name,last_name,age=''):
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
muician=build_person('jimi','hendrix',age=27)
print(muician)



#结合使用函数和while循环
def get_formatted_name(first_name,last_name):
	full_name=first_name+' '+last_name
	return full_name
while True:
	print("\nPlease tell me your name:")
	print("(enter'q' at any time to quit)")
	f_name=input("First name:")
	if f_name=='q':
		break
	l_name=input("Last name:")
	if l_name=='q':
		break
	formatted_name=get_formatted_name(f_name,l_name)
	print("\nHello "+formatted_name+".")