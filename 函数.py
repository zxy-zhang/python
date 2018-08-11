def greet_users():  
#定义函数
	print("hello")
greet_users()        
#函数调用


def greet_users(username):   
#username是一个形参，函数完成工作的一个信息
#向函数传递信息        
	print("Hello,"+username.title()+"!")
greet_users("Bob")    
 #调用函数greet_users()并向他传递信息'Bob'
 #'Bob'是一个实参，调用函数时传递给函数的信息
 


