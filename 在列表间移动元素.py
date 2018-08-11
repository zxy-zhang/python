unconfirmed_users=['alice','brian','candace']  #创建一个待验证用户列表
confirmed_users=[]               #存储已经验证的客户
while unconfirmed_users:
	current_users=unconfirmed_users.pop()     #pop()函数每次一个从列表末尾删除没有验证的客户
	print("Verifying user: "+current_users.title())
	confirmed_users.append(current_users)   #被删除并存储到变量current_user中并加入到列表confirmed_users中
print("\nThe follwing users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())