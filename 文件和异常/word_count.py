def count_words(filename):

	try:
		with open(filename)as file_object:
			contents=file_object.read()
	except FileNotFoundError:
		msg="Sorry,the file "+filename+" doesn't exist."
		print(msg)
	else:
		words=contents.split()
		num_word=len(words)
		print("The file "+filename+" has about    "+str(num_word)+" words.")

filenames=['alice.txt','siddhartha.txt','pi_digits.txt','little_women.txt']
for filename in filenames:
	count_words(filename)

   