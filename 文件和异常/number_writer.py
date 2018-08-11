#存储数据
#用户关闭程序时，总是要保存他们提供的信息，一种简单的方式是用模块json来存储数据
#模块json让你能够将简单的数据结构存储到文件中，并在程序运行时加载该文件的数据
#JSON数据格式并非Python专用的数据，所以和其他语言的人分享
import json
numbers=[2,3,5,7,11,13]

filename='number.json'
with open(filename,'w')as file_object:
	json.dump(numbers,file_object)
	#使用json.dump()来存储数据 