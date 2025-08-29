from modules.api import *
from modules.questions import Questions
from modules.status import Status
from modules.file import Files
from modules.answers import AnswersHelper
# from abc import ABC, abstractmethod

class Quiz:
    def __init__(self, questions: Questions, file: Files,status: Status):
        self.questions = questions
        self.file = file
        self.status = status
        self.answers = AnswersHelper(self.questions.get_questions())
    # @abstractmethod
    def start(self):
        self.status.progress()
        