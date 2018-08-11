for value in range(1,5):
	print(value)            #range()函数从第一个数开始，到指定的第二个值停止，所以输出不包含第二个值

numbers=list(range(1,6))
print(numbers)              #用range()创建数字列表

even_numbers=list(range(2,11,2))  #函数range()从2开始，不断加2，直到超过最终值
print(even_numbers)

squares=[]                  #创建一个空列表
for value in range(1,11):   #遍历1-10的值
	square=value**2         #计算当前值的平方，然后存储到square
	squares.append(square)  #将新计算的平方值加到列表squares末尾
print(squares)              

squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)