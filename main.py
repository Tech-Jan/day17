from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(question)

myquiz = QuizBrain(question_bank)

while myquiz.still_has_questions():
    myquiz.next_question()
print(f"youve completed the quiz! youve {myquiz.score}/{myquiz.question_number}")
