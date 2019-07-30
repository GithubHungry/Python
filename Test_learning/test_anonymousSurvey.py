from unittest import TestCase
from Test_learning.survey import AnonymousSurvey


class TestAnonymousSurvey(TestCase):
    def test_save_answers(self):
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.save_answers('Python')
        self.assertIn('Python', my_survey.answers)

    def test_three_answers(self):
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        answers = ['python', 'c++', 'JS']
        for answer in answers:
            my_survey.save_answers(answer)
        for answer in answers:
            self.assertIn(answer, my_survey.answers)
