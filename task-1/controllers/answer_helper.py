from controllers.files import FileHandler
from controllers.status import Status
from controllers.question_helper import QuestionsHelper
class AnswersHelper:
    def __init__(self,file_handler: FileHandler ,question_helper: QuestionsHelper):
        self._file_handler = file_handler
        self.question_helper = question_helper
        self.current_ans = None

    @property 
    def answer(self):
        return self.current_ans
    @answer.setter
    def answer(self, value: str):
        self.current_ans = value.lower()
    def get_current_answer(self) -> str:
        return self.current_ans
    def get_answer(self, question) -> str:
        return self.questions[question].get("answer", None)
    def check_if_answer_available(self) -> bool:
        question = self.question_helper.get_current_question()
        return question is not None and "ans" in question
    def verify_answer(self) -> bool:
        if not self.check_if_answer_available():
            self.add_answer()
            return True
        else:
            answers = self.question_helper.get_current_question().get("answer", [])
            if self.current_ans in answers:
                return True
        return False

    def check(self) -> bool:
        # Check if the answer is None
        answer = self.current_ans
        question = self.question_helper.current_question
        actual_answer = question.get("answers", None) if question else None
        actual_answer = [a.lower() for a in actual_answer] if actual_answer else []
        if len(actual_answer) == 0:
            return True
        if len(actual_answer) > 0:
            if answer not in list(actual_answer):
                return False
            return True 
