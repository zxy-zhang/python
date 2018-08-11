name=['a','b','c','d']
print(name[0].title())   #title()首字母大写

name=['a','b','c','d']
message="my first name is"+name[0].title()+"."
print(name)               #使用列表的各个值

name=['a','b','c','d']
print(name)
name[0]='f'
print(name)               #修改列表元素

name=['a','b','c','d']
print(name)
name.append('f')
print(name)               #将元素增加到末尾

name=['a','b','c','d']
name.insert(0,'g')
print(name)         #列表中插入元素

name=['a','b','c','d']
print(name)
del name[0]
print(name)         #从列表中删除元素

name=['a','b','c','d']
print(name)
popped_name=name.pop()
print(name)
print(popped_name)   #将元素从列表中删除，并接着使用它的值

name=['a','b','c','d']
print(name)
popped_name=name.pop(2)
print(name)
print(popped_name)       #当使用pop()的时候，被弹出的元素就不在列表中了 如果删除还继续使用就用pop(),反之用del

name=['a','b','c','d']
print(name)
name.remove('a')
print(name)            #不知道要从列表中删除值得所在位置，只知道删除元素的值，可以用方法remove()

name=['a','b','c','d']
print(name)
too_hard='a'
name.remove(too_hard)
print(too_hard+"\tis too hard for me")