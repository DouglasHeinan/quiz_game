from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = create_question_bank()
    right, wrong = ask_question(question_bank)
    print(f"You finished with {right} questions right and {wrong} questions wrong.")
    print("See ya!")


def create_question_bank():
    question_bank = []
    for item in question_data:
        question = Question(item["question"], item["correct_answer"])
        question_bank.append(question)
    return question_bank


def ask_question(question_bank):
    questions = QuizBrain(question_bank)
    while questions.still_has_questions():
        questions.next_question()
    return questions.q_right, questions.q_wrong


if __name__ == "__main__":
    main()