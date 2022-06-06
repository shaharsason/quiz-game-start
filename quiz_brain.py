class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.attempts = 0
        self.q_list = q_list

    def still_has_question(self):
      return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        print(f"category: {current_question.category}")
        print(f"type: {current_question.type}")
        print(f"difficulty: {current_question.difficulty}")
        user_answer = input(f"Q.{self.q_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
            self.attempts += 1
            print(f"your current score is {self.score}/{self.attempts}")
        else:
            self.attempts += 1
            print("thats wrong.")
            print(f"the correct answer was: {correct_answer}")
            print(f"your current score is {self.score}/{self.attempts}")
