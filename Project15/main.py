from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(question_data)) :
    question = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.question_number < len(question_bank):
    quiz.next_question()

print(quiz.game_complete())