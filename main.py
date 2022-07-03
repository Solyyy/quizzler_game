from question_model import Question
from quiz_setup import QuizSetup
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface

quiz_setup = QuizSetup()
total_questions = quiz_setup.get_question_amount()


question_bank = []
for question in quiz_setup.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz, total_questions)
