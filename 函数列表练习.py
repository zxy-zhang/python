# 8-9 魔术师 ： 创建一个包含魔术师名字的列表， 
# 并将其传递给一个名为show_magicians() 的函数， 这个函数打印列表中每个魔术师的名字。  
name_list=['aa','bb','cc']
def show_magicians():
	for name in name_list:
		print(name)
show_magicians()

# 8-10 了不起的魔术师 ： 在你为完成练习8-9而编写的程序中， 编写一个名为make_great() 的函数，   
# 对魔术师列表进行修改， 在每个魔术师的名字中都加入字样“theGreat”。 调用函数show_magicians() ， 确认魔术师列表确实变了。
name_list=['aa','bb','cc']
name_change=[]
def make_greet(name_list,name_change):
	while name_list:
		current=name_list.pop()
		current='the Great '+current
		name_change.append(current)
def show_magicians(name_change):
	for name in name_change:
		print(name)
make_greet(name_list,name_change)
show_magicians(name_change)


# 8-11 不变的魔术师 ： 修改你为完成练习8-10而编写的程序， 在调用函数make_great() 时， 向它传递魔术师列表的副本。   
# 由于不想修改原始列表， 请返回修改后的列表， 并将其存储到另一个列表中。 分别使用这两个列表来调用show_magicians() ，   
# 确认一个列表包含的是原来的魔术师名字， 而另一个列表包含的是添加了字样“the Great”的魔术师名字。  
name_list=['aa','bb','cc']
name_change=[]
def make_greet(name_list,name_change):
	while name_list:
		current=name_list.pop()
		current='the Great '+current
		name_change.append(current)
def show_magicians(name_change):
	for name in name_change:
		print(name)
make_greet(name_list,name_change)
show_magicians(name_list)
show_magicians(name_change)
