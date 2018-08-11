filename='Alice.txt'

try:
	with open(filename)as file_object:
		contents=file_object.read()
except FileNotFoundError:
	msg="Sorry,the file "+filename+" doesn't exist."
	print(msg)


#处理FileNotFoundError
#使用文件时，找不到文件，有可能文件在其他地方，也有可能根本不存在
#由于是open()函数导致的，所以将try放在open()代码之前
#
#计算文件大概包含多少个单词】
#words=contents.split()
#num_words=len(words)
#print("The file "+filename+"has about "+str(num_words)+"wo")