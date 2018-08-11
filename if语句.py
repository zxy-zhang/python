cars=['audio','bwm','subaru','toyota']
for car in cars:
	if car=='bwm':
		print(car.upper())
	else:
		print(car.title())


requested_topping='mushrooms'
if requested_topping!='anvhovies':
	print("Hold the anvhovies!")       #检查是否不相等


banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:            #检查特定值是否不包含在列表中，如果user的值不包含在列表banned_users中，python返回True，进而缩进代码行
	print(user.title()+",you can post a response if you wish.")   
