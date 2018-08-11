from survey import AnonymousSurvey

#定义一个问题，并创建一个调查的AnonymousSurvey对象
question ="What language did you first learn to speak?"
my_survry=AnonymousSurvey(question)

#显示问题并存出答案
my_survry.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
	response=input("Language: ")
	if response=='q':
		break
	my_survry.store_response(response)

#显示调查结果
print("\nThank you to every who participated in the survey!")
my_survry.show_results()