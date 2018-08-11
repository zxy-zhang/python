'''
player=['Yaoming','Liuxiang','charles','martina','michael']
print(player[0:3])
print(player[1:4])
print(player[:4])
print(player[2:])
print(player[-3:])
'''
players=['Yaoming','Liuxiang','charles','martina','michael']
print("Here are the first three players on team:")
for player in players[:3]:
	print(player.title())                  #遍历切片


my_foods=['pizza','falafel','corrt cake']
friend_foods=my_foods[:]                #将my_foods的副本存储到friend_foods
my_foods.append('chocolate')
friend_foods.append('ice cream')
print("My favorite foods are:"+"\n")
print(my_foods)
print("My friend favorite foods are:")
print(friend_foods)                            #复制列表