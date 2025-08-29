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
        self.questions = Questions(file)
        self.status = Status(len(self.questions.get_questions()), self.questions)
        self.answers = AnswersHelper(self.questions.get_questions())

    def create_quiz(self) -> Quiz:
        return Quiz(self.questions, self.file, self.status)

