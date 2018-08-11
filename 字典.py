'''
alien_0={'color':'green','points':5}    #一个简单的字典
print(alien_0['color'])           #访问字典里的值
print(alien_0['points'])

alien_0={'color':'green','points':5} 
new_points=alien_0['points']                     #访问字典alien_0的值
print("You just earned\t"+str(new_points)+"\tpoints!")

alien_0={'color':'green','points':5}                #添加键-值对
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0={}                     #创建空字典，然后分行添加键-值对】
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

alien_0={'color':'green'}
print("The alien is "+alien_0['color']+'.')
alien_0['color']='yellow'
print("The alien now is "+alien_0['color']+".")
'''
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))
alien_0['speed']='fast'             #通过修改字典里的值来改变外星人的行为
#向右移动外星人
#根据外星人的移动速度决定将其移动多远
if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else:
	x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment   #新位置等于老位置加上增量
print("New x_position: "+str(alien_0['x_position']))

alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']              #删除键-值对
print(alien_0)

