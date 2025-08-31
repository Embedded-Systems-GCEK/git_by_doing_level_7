import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controllers.status import Status

data_path = 'data.json'
questions_path = 'questions.json'

class FileHandler():
    def __init__(self, status: "Status"):
        self.data_path = data_path
        self.questions_path = questions_path
        self.datas = None
        self.all_questions = None
        self._all_attempts = 0
        self.status = status
    @property
    def all_attempts(self) -> int:
        if self._all_attempts == 0:
            data = self.data()
            self._all_attempts = data.get("status", {}).get("attempts", 0)
        return self._all_attempts
    @all_attempts.setter
    def all_attempts(self, value: int):
        # May Be used to reset attempts
        self._all_attempts = value

    def _get_file_paths(self, filename: str) -> list:
        """Helper method to get possible file paths"""
        return [
            f"{filename}",
            f"task-1/{filename}"
        ]
    
    def _load_json_file(self, filename: str) -> dict:
        """Helper method to load JSON file with fallback paths"""
        paths = self._get_file_paths(filename)
        try:
            with open(paths[0], 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(paths[1], 'r') as file:
                return json.load(file)
    @property
    def data_path(self):
        return self._data_path
    @data_path.setter
    def data_path(self, path: str):
        self._data_path = path

    @property
    def questions_path(self):
        return self._questions_path
    @questions_path.setter
    def questions_path(self, path: str):
        self._questions_path = path
    
    
    @property
    def questions(self) -> list:
        if self.all_questions is None:
            questions = self._load_json_file(self.questions_path)
            self.all_questions = questions['questions']
            return questions['questions']
        else:
            return self.all_questions

    def data(self):
        if self.datas == None:
            data = self._load_json_file(self.data_path)
            self.datas = data
            return data
        else:
            return self.datas
    @property
    def attempts(self) -> int:
        if self.all_attempts == 0:
            data = self.data()
            self.all_attempts = data.get("status", {}).get("attempts", 0)
        return self.all_attempts
    
    def save_attempts(self, attempts: int):
        data = self.data()
        data["status"]["attempts"] = attempts
        self.save_data(data)
    
    def save_questions(self, questions: list) -> bool:
        """Save the questions data to file"""
        try:
            questions_data = {"questions": questions}
            with open(self.questions_path, 'w') as file:
                json.dump(questions_data, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving questions: {e}")
            return False
    
    def save_data(self, data: dict) -> bool:
        try:
            with open(self.data_path, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        self.datas = data
        return True 
    
    def save_status(self, questions: list) -> bool:
        """Save the current status including progress on questions"""
        try:
            data = self.data()
            
            # Update status with current question progress
            if not data.get("status"):
                data["status"] = {
                    "is_completed": self.status.is_finished,
                    "current_question": self.status.current_question,
                    "attempts": self.status.attempts,
                }
            
            
            return self.save_data(data)
        except Exception as e:
            print(f"Error saving status: {e}")
            return False
    def get_current_question_index(self) -> int:
        data = self.data()
        self.current_question_index = data.get("status", {}).get("current_question", 0)
        return self.current_question_index
    def is_played_before(self) -> bool:
        data = self.data()
        status = data.get("status", {})
        return status.get("attempts", 0) > 0
    def update_question_status(self,question: dict,is_correct:bool):
        for q in self.all_questions:
            if q.get("id",0) == question.get("id",0):
                q["is_asked"] = True
                q["is_answered"] = True
                q["is_correct"] = is_correct
        self.save_questions(self.all_questions)
        return True