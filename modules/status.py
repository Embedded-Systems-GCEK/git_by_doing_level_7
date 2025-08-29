from modules.questions import Questions

class Status:
    def __init__(self,total_questions: int , question_helper: Questions):
        self.total_questions = total_questions
        self.question_helper = question_helper
        self.questions = question_helper.get_questions()
        self.asked_questions = len(question_helper.get_asked_question())
    def remaining(self):
        return len(self.questions) - self.asked_questions
    def evalueate(self):
        pass
    def progress(self):
        print("Status:")
        print(f"Total questions: {self.total_questions}")
        print(f"Asked questions: {self.asked_questions}")
        print(f"Remaining questions: {self.remaining()}")