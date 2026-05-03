class QuizBrain:


    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.total_score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        # return user_answer


    def check_answer(self, user_answer, current_question_answer):
        if user_answer.lower() == current_question_answer.lower():
            print("You got it right!")
            self.total_score += 1
            print(f"SCORE: {self.total_score}/{len(self.question_list)}\n")
            self.next_question()
        else:
            print("That's wrong!")
            print(f"SCORE: {self.total_score}/{len(self.question_list)}\n")
            print(f"The correct answer was: {current_question_answer}\n")