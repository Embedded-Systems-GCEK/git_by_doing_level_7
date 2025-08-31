from controllers.files import FileHandler
from controllers.status import Status
from controllers.question_helper import QuestionsHelper
from controllers.answer_helper import AnswersHelper

class QuizController:
    def __init__(self,file_handler: FileHandler , question_helper: QuestionsHelper,answer_helper: AnswersHelper,status: Status):
        self.file_handler = file_handler
        self.question_helper = question_helper
        self.answer_helper = answer_helper
        self.status = status
        self.is_finished = False
        self.status.attempts = self.file_handler.all_attempts
    def _is_played_before(self) -> bool:
        return self.status.played_before(self.file_handler)
    def intro(self):
        print("Welcome to the Quiz!".center(50, "="))
        print("This is the task-1 of the Level 7    ".center(50, "="))
        print("Before Doing this , you have to start the website".center(50, "="))
        # Check if the website is running by listening to that address
    def initialize(self):
        if self.status.attempts == 0:
            self.intro()
        if self._is_played_before():
            self.status.current_question = self.file_handler.get_current_question_index()
            print("Welcome back!")
        # Get unasked questions 
        else:
            self.status.current_question = 0
        unasked_questions = self.question_helper.get_unasked_questions()
        if len(unasked_questions) == 0:
            print("You have already completed this level.")
            self.status.is_finished = True
            if (self.status.is_finished):
                # TODO: Show status here also
                print("Quiz Finished!")
                print(f"You answered {len(self.question_helper.get_answered_and_correct_questions())} out of {self.question_helper.total_questions} questions correctly.")
            return 
        if self.status.is_finished:
            if self.status.attempts == 0:
                print("error: No attempts made but quiz already finished?. Report it to admins")
                return
            print("Quiz already finished.")
            return
        if self.question_helper.total_questions == 0:
            print("No questions available.")
            return
    def start(self):
        # How to start the quiz
        '''
        - First check the number of questions 
        - Check if the player has already played it before 
        - if true , then check the number of questions he answered,
        - then check the number of correct answers
        - the interate through each question and ask him.
        - Last print the results.
        '''
        self.status.progress()
        while not self.status.is_finished:
            self._ask_next_question()
            is_correct = self.answer_helper.check()
            print(is_correct)
            if is_correct:
                print("Correct Answer!")
                self.status.current_question += 1
                self.file_handler.save_attempts(self.status.attempts)
                self.file_handler.update_question_status(self.question_helper.current_question, is_correct)
            else:
                print("Incorrect Answer!")
    def _ask_next_question(self):
        if self.status.current_question >= self.question_helper.total_questions:
            print("No more questions available.")
            self.status.is_finished = True
            return None
        if self.status.current_question == 0:
            self._ask_questions_by_number(0)
        else:
            self._ask_questions_by_number(self.status.current_question)
        self.status.progress()
        self.status.current_question += 1

    def _ask_questions_by_number(self, question_number: int):
        question = self.question_helper.get_question_by_number(question_number)
        question_text = question.get("question", None) if question else None
        options = question.get("options", []) if question else []
        if question:
            if len(options) > 0:
                # options in ( yes , no ) else " "
                options_str = f"({', '.join(options)})" if options else ""
                prompt = f"Question {question_number + 1}: {question_text} {options_str} " 
                self.answer_helper.answer = input(prompt)
        else:
            print(f"Question {question_number + 1} not found.")
    