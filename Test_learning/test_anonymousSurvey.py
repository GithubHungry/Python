from unittest import TestCase
from Test_learning.survey import AnonymousSurvey


# class TestAnonymousSurvey(TestCase):
#     def test_save_answers(self):
#         question = 'What language did you first learn to speak?'
#         my_survey = AnonymousSurvey(question)
#         my_survey.save_answers('Python')
#         self.assertIn('Python', my_survey.answers)
#
#     def test_three_answers(self):
#         question = 'What language did you first learn to speak?'
#         my_survey = AnonymousSurvey(question)
#         answers = ['python', 'c++', 'JS']
#         for answer in answers:
#             my_survey.save_answers(answer)
#         for answer in answers:
#             self.assertIn(answer, my_survey.answers)


class TestAnonymousSurvey(TestCase):
    def setUp(self):
        question = 'What is your favorite language?'
        self.my_survey = AnonymousSurvey(question)
        self.answers = ['python', 'JS', 'ruby']

    def test_one_answer(self):
        self.my_survey.save_answers(self.answers[0])
        self.assertIn(self.answers[0], self.my_survey.answers)

    def test_three_answers(self):
        for answer in self.answers:
            self.my_survey.save_answers(answer)
        for answer in self.answers:
            self.assertIn(answer, self.my_survey.answers)
