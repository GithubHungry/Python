from Test_learning.survey import AnonymousSurvey

question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)
print("Print 'q' to abort survey.")
while True:
    user_answer = input('Language: ')
    if user_answer == 'q':
        break
    else:
        my_survey.save_answers(user_answer)

print("Thank you !")
my_survey.show_question()
my_survey.show_answers()
