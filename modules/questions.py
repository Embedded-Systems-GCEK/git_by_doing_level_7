import json
# from file import Files
from modules.file import Files

class Questions:
    def __init__(self,file: Files):
        self.file = file
    def get_questions(self) -> list:
        file_contents = self.file.get_questions()
        self.questions = file_contents.get("questions", [])
        return self.questions
    def get_num_questions(self) -> int:
        return len(self.questions)
    def get_n_th_question(self, n: int) -> dict | None:
        for question in self.questions:
            if question['id'] == n:
                return question
        return {}
    def get_asked_question(self) -> list:
        return [q for q in self.questions if q.get('is_asked', False)]
    def get_normal_question_prompt(self, question, number):
        options_len = len(question['options'])
        options = question['options'] if options_len > 0 else ""
        show_options = ' or '.join([i for i in list(options) if len(options) > 0])
        alt_show_options = f"({show_options})" if len(show_options) > 0 else ""
        return f"Question {number}: {question['question']} {alt_show_options} "

    def ask_question_by_number(self,n):
        question = self.get_n_th_question(n)
        return input(self.get_normal_question_prompt(question, n))