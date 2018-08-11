filename='pi_digits.txt'
#将读取的文件额名称存储在变量filename中

with open(filename)as file_object:
	#调用open()后，将一个表示文件及其内容的对象存储在变量file_object中
	for line in file_object:
		#循环遍历文件中的每一行
		print(line.rstrip())