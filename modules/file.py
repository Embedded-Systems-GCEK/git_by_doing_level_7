import json
data_file_path = "data.json"

class Files:
    def __init__(self,file_path):
        self.file_path = file_path
    def get_questions(self):
        with open(self.file_path, 'r') as file:
            questions = json.load(file)
            return questions
    def save_answer(self, answer: str, question: dict):
        with open(self.file_path, 'r+') as file:
            data = json.load(file)
            for q in data:
                if q["id"] == question["id"]:
                    q["answer"] = answer
            file.seek(0)
            json.dump(data, file)
            file.truncate()
    def get_status(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return data.get("status", {})