
from controllers.files import FileHandler


class QuestionsHelper():
    def __init__(self,file_handler: FileHandler):
        self._file_handler = file_handler
        self._total_questions = len(self._file_handler.questions)
        self._current_question = {}
    @property
    def current_question(self) -> dict:
        return self._current_question
    @current_question.setter
    def current_question(self, question: dict):
        self._current_question = question
    @property
    def total_questions(self) -> int:
        return self._total_questions
    @total_questions.setter
    def total_questions(self,value):
        self._total_questions = value
    def get_unasked_questions(self):
        return [q for q in self._file_handler.questions if not q.get("is_asked", False)]
    def get_answered_and_correct_questions(self):
        return [q for q in self._file_handler.questions if q.get("is_answered", False) and q.get("is_correct", False)]
    def get_question_by_number(self, question_number: int):
        if 0 <= question_number < self._total_questions:
            for q in self._file_handler.questions:
                if q.get("id",0) == question_number:
                    self.current_question = q
                    return q
        print("Question Not Available")
        return None