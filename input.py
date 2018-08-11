'''
name=input("Please enter your name:")
print("Hello,"+name+"!")

prompt="hello,"
prompt+="What is your name?"        #在prompt中的字符喘末尾加一个字符串
name=input(prompt)
print("\nHello,"+name+"!")          #最终的提示横跨两行 
'''

height=input("how tall are you,in inches?")
height=int(height)                      #将数值用于计算和比较前，务必将其转化为数值表示
if height>=36:
	print("\nYou are tall enough to ride!")

