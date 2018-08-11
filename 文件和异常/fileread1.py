file_path=(r'C:\Users\zxy\Desktop\python\文件和异常\python——work\filename_work.txt')
with open(file_path)as file_object:
	contents=file_object.read()
	print(contents.rstrip())