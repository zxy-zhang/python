magicians=['Jack','Bob','Tom']
for magician in magicians:
	print(magician)               #遍历列表，对每个元素执行相同的操作

magicians=['Jack','Bob','Tom']
for magician in magicians:
	print(magician.title()+",that was a great trick!")
	print("I can't wait to see your next trick,"+magician.title()+"\n")   #在for循环中执行更多的操作

print("Thank you ,everyone.that was a great magic show!")   #这条语句没有缩进，所以只执行一次
