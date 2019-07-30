class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.answers = []

    def show_question(self):
        print(self.question)

    def save_answers(self, answer):
        self.answers.append(answer)

    def show_answers(self):
        print('Results: ')
        for answer in self.answers:
            print("- " + answer)
