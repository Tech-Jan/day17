class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question2(self):
        score = 0
        for question in self.question_list:
            self.question_number += 1
            if input(f"Q. {self.question_number}: {question.text} [True or False] ") == question.answer:
                score += 1
                print(f"gj \nThe Correct answer was {question.answer}\n your score is {score}/{self.question_number}")
            else:
                print("sry wrong answer")
                print(f"gj \nThe Correct answer was {question.answer}\n your score is {score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}/{len(self.question_list)}: {current_question.text}"
                            f" [True or False] ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("your answer was right")
            self.score += 1
        else:
            print("thats wrong")
        print(f"the serached answer was {correct_answer}")
        print(f"{self.score}/{self.question_number}")
        print("\n")
