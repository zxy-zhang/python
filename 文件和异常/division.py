# print("Give me two numbers ,and i'll divide them.")
# print("Enter 'q' to quit.")

# while True:
# 	first_number=input("\nFirst number: ")
# 	if first_number=='q':
# 		break

# 	second_number=input("second_number: ")
# 	if second_number=='q':
# 		break

# 	answer=int(first_number)/int(second_number)
# 	print(answer)




print("Give me two numbers ,and i'll divide them.")
print("Enter 'q' to quit.")	

while True:
	first_number=input("\nFirst number: ")
	if first_number=='q':
		break

	second_number=input("\nSecond number: ")
	try:
		answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0")
	else:
		print(answer)

#错误是执行运算代码导致的，所以将她放到try_except代码块中
#还包含一个else代码块，依赖于try代码块成功执行的代码都应该放到else代码块中