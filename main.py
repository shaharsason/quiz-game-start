from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    question_type = question["type"]
    question_difficulty = question["difficulty"]
    new_question = Question(question_text, question_answer, question_category, question_type, question_difficulty)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question() == True:
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score was {quiz.score}/{quiz.attempts}")
