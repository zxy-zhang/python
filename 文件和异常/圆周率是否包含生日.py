filename='pi_million_digits.txt'

with open(filename)as file_object:
	lines=file_object.readlines()

pi_string=''
for line in lines:
	pi_string+=line.strip()

birthday=input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in hte first millions digits of pi!")
else:
	print("Your birthday doesn't appears in hte first millions digits of pi!")