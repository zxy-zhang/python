current_number=0
while current_number<10:
	current_number+=1
	if current_number%2==0:
		continue
	print(current_number)


#避免无限循环，可以按Ctrl+c停止循环，也可以关闭终端窗口
#编辑器内嵌窗口，基本只能关闭编辑器来终止循环