import json
from modules.file import Files

class Questions:
    def __init__(self,file: Files):
        self.file = file
        self.current_question = None
        self.current_question_number = 0
    def current_question(self) -> dict | None:
        return self.current_question
    def all_questions(self) -> list:
        file_contents = self.file.get_questions()
        self.questions = file_contents.get("questions", [])
        return self.questions
    def total_questions(self) -> int:
        return len(self.questions)
    def get_n_th_question(self, n: int) -> dict | None:
        for question in self.questions:
            if question['id'] == n:
                return question
        return {}
    def asked_question(self) -> list:
        return [q for q in self.all_questions() if q.get('is_asked', False)]
    def get_normal_question_prompt(self, question, number):
        options_len = len(question['options'])
        options = question['options'] if options_len > 0 else ""
        show_options = ' or '.join([i for i in list(options) if len(options) > 0])
        alt_show_options = f"({show_options})" if len(show_options) > 0 else ""
        return f"Question {number}: {question['question']} {alt_show_options} "

    def ask_question_by_number(self,n):
        question = self.get_n_th_question(n)

        self.current_question = question
        self.current_question_number = n
        return input(self.get_normal_question_prompt(question, n))
    def get_follow_up(self):
        if self.current_question and "follow_up" in self.current_question.keys():
            return self.current_question["follow_up"]
        return {}
    def check_if_follow_up(self) -> bool:
        return True if self.current_question and "follow_up" in self.current_question.keys() else False
    def ask_follow_up(self):
        follow_ups = self.get_follow_up()
        follow_up_answers = {}
        for key, follow_up in follow_ups.items():
            answer = input(f"Follow-up question: {follow_up} ")
            follow_up_answers[key] = answer
        return follow_up_answers
    def check_if_already_asked(self, n):
        return self.questions[n].get('is_asked', False)