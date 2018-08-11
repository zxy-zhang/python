message=input("What kinds of the car go you want?")    
print("Let me see if i can find you a "+message)


customer_number=input("How many people have dinner?")
customer_number=int(customer_number)
if customer_number>8:
	print("sorry,we have no empty table")
else:
	print("we have empty tables")

number=input("Enter a number:")        #判断输入的数是否为整数
number=int(number)
if number%10==0:
	print("True")
else:
	print("False")