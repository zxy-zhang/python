pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
    }
print("You ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
	print("\t"+topping)


favorite_languages={                   #每个名字关联的值都是一个列表
	'jen':['python','rubby'],
	'sarch':['c'],
	'edwrd':['ruby','go'],
	'phil':['python','haskell'],
    }
for name,languages in favorite_languages.items():
	if len(languages)==1:                  #确定列表元素是否为一个
		print("\n"+name.title()+"'s favorite language is:")
	else:
		print("\n"+name.title()+"'s favorite languages are:")
	for language in languages:
		print("\t"+language.title())
