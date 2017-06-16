import random

input_file = 'question.txt'
quantity_questions = 10

def create_dict_questions(input_file, quantity_questions):
    questions = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        number_question = 1
        while number_question <= quantity_questions:
            question = file.readline().replace('\n','')
            opinion1 = file.readline().replace('\n','')
            opinion2 = file.readline().replace('\n','')
            opinion3 = file.readline().replace('\n','')
            opinion4 = file.readline().replace('\n','')
            correct_answer = opinion1
            question_next =\
                {'question': question,
                 'answers': [opinion1, opinion2, opinion3, opinion4],
                 'correct_answer': correct_answer}
            questions['Number %d' % number_question] = question_next
            number_question += 1
    return questions

questions = \
    create_dict_questions(input_file, quantity_questions).copy()

def interview(questions):
    review = None
    print('Hello, you have an unique opportunity' + \
           ' to take the this test about Python !!!')
    ready = input('When you want to start, press 1')
    with open('results.txt', 'w', encoding='utf-8') as results:
        user_name = input('Please write your name  ')
        results.write('Result ' + user_name + ' skills from Python')
    right_answers = 0
    for i in range(1, quantity_questions + 1):
        print(questions['Number %d' % i]['question'])
        correct_answer = questions['Number %d' % i]['correct_answer']
        answers = random.sample(questions['Number %d' % i]['answers'],\
                  len(questions['Number %d' % i]['answers']))
        for j in range(4):
            print('Possible answers is: ')
            print(answers[j])
            users_answer = input('If you think that this opinion is' +\
                                 ' correct enter 1, else 2   ')
            if (questions['Number %d' % i]['correct_answer'] == answers[j])\
                and users_answer == '1':
                right_answers += 1
                if i != quantity_questions:
                    print('Ok, Next question' + '\n')
                    with open('results.txt', 'a', encoding='utf-8') as results:
                        results.write('\n')
                        results.write('Question %d:' % i)
                        results.write('\n')
                        results.write(questions['Number %d' % i]['question'])
                        results.write('\n')
                        results.write(user_name + ' answer: ' + answers[j] +\
                                      ' is correct')
                break
            elif (questions['Number %d' % i]['correct_answer'] != answers[j])\
                  and users_answer == '1':
                if i != quantity_questions:
                    print('Ok, Next question' + '\n')
                    with open('results.txt', 'a', encoding='utf-8') as results:
                        results.write('\n')
                        results.write('Question %d:' % i)
                        results.write('\n')
                        results.write(questions['Number %d' % i]['question'])
                        results.write('\n')
                        results.write(user_name + ' answer: ' + answers[j] + \
                                      ' is incorrect')
                break
    else:
        print('The end')
        print('Thank you for your time')
    with open('results.txt', 'a', encoding='utf-8') as results:
        results.write('\n')
        results.write('Results ' + str(user_name) + ' is:')
        results.write('right_answers = ' + str(right_answers) + ' from ' +\
                      str(quantity_questions))
        results.write('\n' + 'Thank you')

    review = 'You have right_answers ' + str(right_answers) + ' from ' +\
             ' ' + str(quantity_questions) + '\n' + user_name +\
             ' you have the potential!'
    return review

#print(interview(questions))
#######