from collections import OrderedDict
favorite_languages=OrderedDict()


favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['tom']='java'
favorite_languages['phil']='python'


for name,languages in favorite_languages.items():
	print(name.title()+"'s favorite language is "+languages.title()+".")
	