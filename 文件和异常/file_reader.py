with open('pi_digits.txt')as file_object:
	contents=file_object.read()
	print(contents)

#运行结果多出个空行，是因为read()到达文件末尾时返回夜歌空字符串，而这个空字符串显示出来就是一个空行
#删除这个空行，在print语句中使用rstrip()
with open('pi_digits.txt')as file_object:
	contents=file_object.read()
	print(contents.rstrip())

