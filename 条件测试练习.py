food='pizza'
print(food=='pizza')
print(food=='apple')

food='apple'
foods=food.lower()
print(foods=='apple')   #使用函数lower()的测试
print(foods=='pear')

foods_kind=['apple','pear','banana','orange']
kind='apple'
if kind in foods_kind:
	print(kind.title()+"\tis pretty good")

foods_kind=['apple','pear','banana','orange']
kind='tomato'
if kind not in foods_kind:
	print(kind.title()+"\tis not suit for me")
