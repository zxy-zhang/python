user_0={
    'username':'zxy',
    'first': 'zz',
    'last':'xy',
	}
for key,value in user_0.items():
	print("\nKey: "+key)
	print("value: "+value)


favorite_numbers={
	'Jack':6,
	'Bob':7,
	'Tom':8
    }
for name,number in favorite_numbers.items():
	print(name.title()+"'s favorite number is "+str(number)+".")


favorite_numbers={
	'Jack':6,
	'Bob':7,
	'Tom':8
    }
for name in favorite_numbers.keys():        #遍历字典的所有键
	print(name.title())


favorite_numbers={
	'Jack':6,
	'Bob':7,
	'Tom':8
    }
friend=['Tom']
for name in favorite_numbers.keys():
	print(name.title())
	if name in friend:
		print("Hi,"+name.title()+",I see your favorite number is "+str(favorite_numbers[name])+"!")


favorite_numbers={
	'Jack':6,
	'Bob':7,
	'Tom':8
    }
for name in sorted(favorite_numbers.keys()):        #函数sorted()对返回的键按特定顺序进行排序
	print(name.title()+",thank you")


favorite_numbers={                             #提取字典的每个值，不考虑是否重复
	'Jack':6,
	'Bob':7,
	'Tom':8                        
    }
for number in favorite_numbers.values():
	print(number)



favorite_numbers={
	'Jack':6,
	'Bob':7,
	'Tom':8
    }
for number in set(favorite_numbers.values()):    #函数set()可以找出列表独一无二的元素，并且使用这些元素来创建一个集合
	print(number)

