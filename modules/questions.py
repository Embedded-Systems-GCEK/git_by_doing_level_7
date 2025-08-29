import json

def get_questions():
    with open('modules/questions.json', 'r') as file:
        questions = json.load(file)
        return questions
def get_n_th_question(questions , n):
    for question in questions['questions']:
        if question['id'] == n:
            return question
    return None

def ask_questions():
    questions = get_questions()
    total_questions = len(questions['questions'])
    print("There are ", total_questions, "questions in total")
    for i in range(total_questions):
        if questions['questions'][i]['is_asked']:
            print("Question has already been asked.")
            if questions['questions'][i]['is_correct']:
                print("The answer was correct.")
            continue
        answer = ask_question_by_number(questions,i)
        if get_n_th_question(questions,i)['answers'][0] == "":
            get_n_th_question(questions,i)['answers'].remove("")
            get_n_th_question(questions,i)['answers'].append(answer)
        else:
            if answer.lower() in [a.lower() for a in list(get_n_th_question(questions,i)['answers'])]:
                print("Correct!")
                questions['questions'][i]['is_correct'] = True
                questions['questions'][i]['is_asked'] = True
    json_object = json.dumps(questions, indent=4)
    with open('modules/questions.json', 'w') as file:
        file.write(json_object)

def get_question_text(question,n):
    options_len = len(question['options'])
    options = question['options'] if options_len > 0 else ""
    show_options = ' or '.join([i for i in list(options) if len(options) > 0])
    alt_show_options = f"({show_options})" if len(show_options) > 0 else ""
    return f"Question {n}: {question['question']} {alt_show_options} "

def ask_question_by_number(questions,n):
    question = get_n_th_question(questions, n)
    return input(get_question_text(question,n))