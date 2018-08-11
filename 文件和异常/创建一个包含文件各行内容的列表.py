#使用关键字with时。open()返回的文件对象只在with代码块中使用
#如果要在with代码块外访问文件的内容，可在with代码块内将文件各行存储在一个列表中，并在with代码块外使用该列表
#可以立即处理文件的各个部分，也可推迟到程序后面处理

filename='pi_digits.txt'

with open(filename)as file_object:
	lines=file_object.readlines()
	#方法readlines()从文件中读取每一行并将其存储在一个列表中

for line in lines:
	print(line.rstrip())