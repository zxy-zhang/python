filename='pi_digits.txt'

with open(filename)as file_object:
	lines=file_object.readlines()

pi_string=''
#用于存储文件的值
for line in lines:
	pi_string+=line.rstrip()
	#使用循环将各行都加入pi_string，并删除末尾的换行符

print(pi_string)
print(len(pi_string))



filename='pi_digits.txt'
with open(filename)as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.strip()
	#在使用pi_string存储的字符串中，包含原来位于每行左边的空格，用strip()可以删除这些空格

print(pi_string)
print(len(pi_string))


#打印到小数点后50位
filename='pi_million_digits.txt'

with open(filename)as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.strip()

print(pi_string[:52]+"...")
print(len(pi_string))

