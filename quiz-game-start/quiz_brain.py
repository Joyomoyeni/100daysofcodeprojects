class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
    def still_has_questions(self):
        if(self.question_number < len(self.question_list)):
            return True
        else:
            return False
    def next_question(self):
        quest = (self.question_list[self.question_number])
        current_question = quest.text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False)?: ")
        self.check_answer(user_answer, quest.answer)
    def check_answer(self, user, correct):
        if(user == correct):
            self.score += 1
            print("You got it right")
            print(f"The correct answer is {correct}")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"The correct answer is {correct}")
            print(f"Your current score is: {self.score}/{self.question_number}")

