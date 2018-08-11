name_list=['Tom','Jack','Bob','Alice']
message_1="welcome\t"+name_list[0]+"."+"\n"
message_2="welcome\t"+name_list[1]+"."+"\n"
message_3="welcome\t"+name_list[2]+"."+"\n"
print(message_1+message_2+message_3)
print(name_list[0]+"\tcan't come")
name_list[0]='Jerry'
message_1="welcome\t"+name_list[0]+"."+"\n"
message_2="welcome\t"+name_list[1]+"."+"\n"
message_3="welcome\t"+name_list[2]+"."+"\n"
print(message_1+message_2+message_3)
print("I found a bigger table")
name_list=['Jerry','Bob','Alice']
name_list.insert(0,'daman')
name_list.insert(2,'max')
name_list.append('mike')
message_1="welcome\t"+name_list[0]+"."+"\n"
message_2="welcome\t"+name_list[1]+"."+"\n"
message_3="welcome\t"+name_list[2]+"."+"\n"
message_4="welcome\t"+name_list[3]+"."+"\n"
message_5="welcome\t"+name_list[4]+"."+"\n"
message_6="welcome\t"+name_list[5]+"."+"\n"
print(message_1+message_2+message_3+message_4+message_5+message_6)
print("sorry,the table can't be sent on time,I just invite 2 person to come")
quxiao=name_list.pop()
print("sorry,"+quxiao+"\tI can't invite you")
quxiao=name_list.pop()
print("sorry,"+quxiao+"\tI can't invite you")
quxiao=name_list.pop()
print("sorry,"+quxiao+"\tI can't invite you")
quxiao=name_list.pop()
message_1="congratulations\t"+name_list[0]+"\tyou still can come"+"."+"\n"
message_2="congratulations\t"+name_list[1]+"\tyou still can come"+"."+"\n"
print(message_1+message_2)
name_list=message_1+message_2
print(name_list)


