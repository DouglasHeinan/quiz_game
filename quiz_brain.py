import random


class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 1
        self.q_right = 0
        self.q_wrong = 0
        self.question_list = q_list

    def next_question(self):
        cur_q = random.choice(self.question_list)
        answer = input(f"Q.{self.q_num}: {cur_q.text} (Answer True or False) ")
        self.check_answer(answer, cur_q)
        self.q_num += 1
        self.question_list.remove(cur_q)

    def still_has_questions(self):
        return self.q_right + self.q_wrong < 10

    def check_answer(self, answer, cur_q):
        while answer.upper() != "TRUE" and answer.upper() != "FALSE":
            print(f"Please answer True or False only: ")
            answer = input(f"Q.{self.q_num}: {cur_q.text} (Answer True or False) ")
        if answer.upper() == cur_q.answer.upper():
            self.q_right += 1
            print(f"Good job! Right:{self.q_right} Wrong:{self.q_wrong}")
        else:
            self.q_wrong += 1
            print(f"Nope. Right:{self.q_right} Wrong:{self.q_wrong}")
