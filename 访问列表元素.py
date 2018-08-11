'''
bicycle=['a','b','c','d']
print(bicycle[0].title())      #索引从0开始而不是从1开始

bicycle=['a','b','c','d']
print(bicycle[0].title())
bicycle[0]='e'
print(bicycle)              #修改列表元素

bicycle=['a','b','c','d']
print(bicycle[0].title())
bicycle.append('f')
print(bicycle)      #在列表中增加元素

bicycle=['a','b','c','d']
bicycle.insert(0,'f')
print(bicycle)         #在列表中插入元素

bicycle=['a','b','c','d']
del bicycle[1]
print(bicycle)          #在列表中删除元素


bicycle=['a','b','c','d']
print(bicycle)
popped_bicycle=bicycle.pop()
print(bicycle)
print(popped_bicycle)
#pop()删除列表末尾的元素   弹出列表任何位置的元素在括号内添加位置的索引
'''
bicycle=['a','b','c','d']
print(bicycle)
bicycle.remove('a')
print(bicycle)           #根据值删除元素，不知道值得位置，只知道删除元素的值，可以使用方法remove()
