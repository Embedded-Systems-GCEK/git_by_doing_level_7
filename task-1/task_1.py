from modules.file import Files
from modules.questions import Questions
from factory.task_factory import TaskFactory
questions_path = 'questions.json'
file = Files(questions_path)

def main():
    task_factory = TaskFactory(file)
    quiz = task_factory.create_quiz()
    quiz.start()
    quiz.ask_questions()
    quiz.save_results()
    quiz.cool()
if __name__  == "__main__":
    main()
