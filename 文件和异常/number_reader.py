import json

filename='number.json'
with open(filename)as file_object:
	numbers=json.load(file_object)

print(numbers)

#函数json.load()加载存储在numbers,json中的信息。并将其存储到变量numbers中