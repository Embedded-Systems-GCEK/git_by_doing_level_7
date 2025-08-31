# Task 1 of the Level 7
from controllers.files import FileHandler
from controllers.status import Status
from controllers.question_helper import QuestionsHelper
from controllers.answer_helper import AnswersHelper
from controllers.quiz import QuizController as Q


status = Status()
files = FileHandler(status=status)
question_helper = QuestionsHelper(files)
answer_helper = AnswersHelper(file_handler=files, question_helper=question_helper)

quiz = Q(file_handler=files, status=status, question_helper=question_helper, answer_helper=answer_helper)

quiz.initialize()
quiz.start()
# quiz.file_handler.save()
# quiz.done()
