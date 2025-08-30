from modules.answers import AnswersHelper
from modules.questions import Questions
from abstract.status import AbstractStatus 

class Status(AbstractStatus):
    def __init__(self, question_helper: Questions, answers_helper: AnswersHelper):
        # Get number of questions from , question_helper
        self.question_helper = question_helper
        self.answers_helper = answers_helper
        # list of questions that are already asked
        self.asked_questions = len(question_helper.asked_question())
    def completed(self) -> bool:
        return len(self.asked_questions) == self.question_helper.total_questions()
    def already_played(self) -> bool:
        return len(self.asked_questions) > 0
    def remaining(self):
        return self.question_helper.remaining_questions()
    def progress(self):
        print("Status:")
        print(f"Total questions: {self.question_helper.total_questions()}")
        print(f"Asked questions: {self.asked_questions}")
        print(f"Current question: {self.question_helper.current_question_number}")
        print(f"Remaining questions: {self.remaining()}")