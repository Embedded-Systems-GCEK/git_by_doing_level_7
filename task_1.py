from modules.file import Files
from modules.questions import Questions
from factory.task_factory import TaskFactory
questions_path = 'modules/questions.json'
file = Files(questions_path)

# def ask_questions():
#         questions = get_questions()
#         total_questions = len(questions['questions'])
#         print("There are ", total_questions, "questions in total")
#         for i in range(total_questions):
#             if questions['questions'][i]['is_asked']:
#                 print("Question has already been asked.")
#                 if questions['questions'][i]['is_correct']:
#                     print("The answer was correct.")
#                 continue
#             answer = ask_question_by_number(questions,i)
#             if get_n_th_question(questions,i)['answers'][0] == "":
#                 get_n_th_question(questions,i)['answers'].remove("")
#                 get_n_th_question(questions,i)['answers'].append(answer)
#             else:
#                 if answer.lower() in [a.lower() for a in list(get_n_th_question(questions,i)['answers'])]:
#                     print("Correct!")
#                     questions['questions'][i]['is_correct'] = True
#                     questions['questions'][i]['is_asked'] = True
#         json_object = json.dumps(questions, indent=4)
#         with open('modules/questions.json', 'w') as file:
#             file.write(json_object)

#     def get_question_text(question,n):
#         options_len = len(question['options'])
#         options = question['options'] if options_len > 0 else ""
#         show_options = ' or '.join([i for i in list(options) if len(options) > 0])
#         alt_show_options = f"({show_options})" if len(show_options) > 0 else ""
#         return f"Question {n}: {question['question']} {alt_show_options} "




def main():
    task_factory = TaskFactory(file)
    quiz = task_factory.create_quiz()
    quiz.start()
    len_quiz = quiz.questions.get_num_questions()
    for num in range(len_quiz):
         ans = quiz.questions.ask_question_by_number(num)
         quiz.answers.verify_and_add_answer(num,ans)
         quiz.questions.check_if_follow_up(quiz.questions.get_current_question())
         quiz.status.progress()
    quiz.cool()

if __name__  == "__main__":
    main()
