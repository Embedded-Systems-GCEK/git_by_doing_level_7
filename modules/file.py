import json

class Files:
    def __init__(self,file_path):
        self.file_path = file_path
    def get_questions(self):
        with open(self.file_path, 'r') as file:
            questions = json.load(file)
            return questions
