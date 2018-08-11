age=19
if age>=18:
	print("Your are old enough to vote")

age=17
if age>=18:
	print("You are old enough to vote")
	print("Have you registered to vote yet?")              #if-else语句
else:
	print("You are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


age=12
if age<4:
	print("Your admission cost is $0.")
elif age<18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")


age=12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10
print("Your admission is cost $"+str(price)+".")


requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:                               #测试多个条件
	print("Adding mushrooms!")
if 'pepperonis' in requested_toppings:
	print("Adding pepperonis!")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese!")
print("\nFinish making your pizza")


requested_toppings=['mushrooms','green peppers','extra cheese']   #检查特殊元素
for requested_topping in requested_toppings:
	if requested_topping=='green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding\t"+requested_topping+".")
	print("\nFinished making your pizza!")

requested_toppings=[]                                #确定列表是不是空的，如果不是空的，将输出列表的元素
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding"+requested_topping+".")
	print("\nFinsished making your pizza.")
else:
	print("Are you sure you want a plain pizza?")


avaliable_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in avaliable_toppings:
		print("Adding\t"+requested_topping+".")
	else:
		print("We don't have"+requested_topping+".")
print("\tFinished making your pizza!requested_toppings=['mushrooms','extra cheese']")