users={                             #定义一个名为users的字典
	'aeinstein':{
	'first':'albert',
	'last':'aeinstein',
	'location':'princetion',
	},
	'curie':{
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
    }
for username,user_info in users.items():       #遍历字典users，让python依次将每个键存储在变量username中，并依次将与当前键相关联的字典存储在变量user_info中
	print("\nUserName"+username)
	full_name=user_info['first']+""+user_info['last']
	location=user_info['location']
	print("\tFull name: "+full_name.title())
	print("\tLocation: "+location.title())