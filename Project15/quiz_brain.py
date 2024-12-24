class QuizBrain :
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.choice = None
        self.score = 0
    
    def next_question(self) :
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.choice = input(f"Q.{self.question_number} {current_question.text} (True/False)\n").lower()
        print(self.score_checking(current_question))

    
    def score_checking(self, current_question) :
        if self.choice.lower() == current_question.answer.lower() :
            self.score += 1
            return f"Score is {self.score}/{self.question_number}"
        else :
            return f"Score is {self.score}/{self.question_number}"
        
    def game_complete(self) :
        return f"You Completed The Quiz Your Score is: {self.score}/{self.question_number}"

