'''
squares=[value**2 for value in range(1,11)]   
print(squares)

numbers=[value for value in range(1,21,2)]
print(numbers)
'''
for i in range(3,31):           #被3整除
	if i%3==0:
		print(i,end="\t")

numbers=[value**3 for value in range(1,11)]
print(numbers)

cube_numbers=[value**3 for value in range(1,11)]#解析一个列表，包含前十个整数的立方
for cube_number in cube_numbers:
     print(cube_number,end="\t")                    

