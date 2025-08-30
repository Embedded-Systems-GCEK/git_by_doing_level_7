from modules.api import *
from modules.questions import Questions
from modules.status import Status
from modules.file import Files
from modules.answers import AnswersHelper
from abc import ABC, abstractmethod
from factory.quiz import Quiz


class TaskFactory:
    def __init__(self,file: Files):
        self.file = file
        self.questions_helper = Questions(file)
        self.answers_helper = AnswersHelper(question_helper=self.questions_helper)
        self.status = Status(question_helper=self.questions_helper, answers_helper=self.answers_helper)

    def create_quiz(self) -> Quiz:
        return Quiz(self.questions_helper, self.file, self.status)

