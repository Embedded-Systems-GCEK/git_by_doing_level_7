from modules.api import *
from modules.questions import Questions
from modules.status import Status
from modules.file import Files
from modules.answers import AnswersHelper
from abc import ABC, abstractmethod


class AbstractQuiz(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def ask_questions(self):
        pass

    @abstractmethod
    def cool(self):
        pass

class Quiz(AbstractQuiz):
    def __init__(self, questions: Questions, file: Files,status: Status):
        self.questions_helper = questions
        self.file = file
        self.status = status
        self.answers_helper = AnswersHelper(question_helper=self.questions_helper)
        self.len_quiz = 0
 
    # Check if they have already played the quiz
    def start(self):
        self.status.progress()
        self.len_quiz = self.questions_helper.get_num_questions()
        user_status = self.file.get_status()
        is_completed = user_status.get("is_completed", False)
        if is_completed:
            print("You have already completed the quiz.")
            return
    def ask_questions(self):
        for num in range(self.len_quiz):
            if self.questions_helper.check_if_already_asked(num):
                continue
            else:
                ans = self.questions_helper.ask_question_by_number(num)
                self.answers_helper.verify_answer(num, ans)
            self.file.save_answer(self.answers_helper.get_current_answer(), self.questions_helper.get_current_question())
    
        