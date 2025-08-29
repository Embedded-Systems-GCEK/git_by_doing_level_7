import json
with open("modules/questions.json") as f:
    questions = json.load(f)



class Answers:
    def __init__(self,questions):
        self.questions = questions
    def add_answer(self, question, answer):
        self.questions[question]["ans"] = answer

    def get_answer(self, question):
        return self.questions[question].get("ans", None)
    def check_if_follow_up(self):
        print(list(self.questions["questions"]))
        for question in list(se)
# def check_if_follow_up(question):
#     for q in questions["questions"]:
#         if q["question"] == question and "follow_up" in q:
#             return True
#     return False

# def get_optional_questions():
#     optional_questions = []
#     for q in questions["questions"]:
#         if "follow_up" in q:
#             for follow_up in q["follow_up"].values():
#                 optional_questions.append(follow_up)
#     return optional_questions

if __name__ == "__main__":
    ans = Answers(questions)
    ans.check_if_follow_up()