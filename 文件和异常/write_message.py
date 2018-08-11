filename='programming.txt'
'''
with open (filename,'w')as file_object:
	#调用函数open()写了两个实参，第一个是要打开的文件，第二个是告诉python用写入模式打开
	#读取模式（'r'）,写入模式('w'),附加模式('a')
	#读取和写入文件的模式('r+')
	#省略实参，按照只读模式打开文件
	file_object.write("I love programming!\n")
	file_object.write("I love creating games!\n")


	#python只能将字符串写入文本文件，要将数值数据存储到文本文件中，必须str()转换为字符串模式
	'''
with open(filename,'a')as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
	#打开文件指定实参a，写入两行，添加到programming.txt末尾