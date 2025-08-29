import json
from modules.questions import Questions
class AnswersHelper:
    def __init__(self,question_helper: Questions):
        self.question_helper = question_helper
        self.current_ans = None
    def get_current_answer(self) -> str:
        return self.current_ans
    def add_answer(self) -> bool:
        self.question_helper.get_current_question()["answer"] = self.current_ans
        return True
    def get_answer(self, question) -> str:
        return self.questions[question].get("answer", None)
    def check_if_answer_available(self) -> bool:
        question = self.question_helper.get_current_question()
        return question is not None and "ans" in question
    def verify_answer(self, answer: str) -> bool:
        self.current_ans = answer
        if not self.check_if_answer_available():
            self.add_answer()
            return True
        else:
            answers = self.question_helper.get_current_question().get("answer", [])
            if answer in answers:
                self.current_ans = answer
                return True
        return False
