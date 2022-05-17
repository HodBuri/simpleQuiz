import random

def getQuestionList():
    questionList = [{'Q':'What is an INTEGER(int)','A':'Whole-valued positive or negative number or 0'},
                     {'Q':'What is a DOUBLE','A':'A 64-bit floating data type'},
                     {'Q':'What is a FLOAT','A':'A number that has a decimal place'},
                     {'Q':'What is a BOOL','A':'A value that represents True or False',},
                     {'Q':'What is a STRING(str)','A':'An array of characters ["s","t","r"]'},
                     {'Q':'What is a CHARACTER(cha)','A':'A single symbol like "A"'},
                     {'Q':'What is a TUPLE','A':'An Array of elements that is immutable'},
                     {'Q':'What is a LIST','A':'An Array of elements that is mutable'},
                     {'Q':'What is an ARRAY','A':'A data structure consisting of a collection of elements'},
                     {'Q':'What is a DICT/MAP','A':'An associative array'},
                     {'Q':'What is a NULL value','A':'Nothing,Zero,Missing Data'},
                     {'Q':'What is a VARIABLE(var)','A':'A data type that can change'},
                     {'Q':'What is an IF statement','A':'A statement that checks if something is True'},
                     {'Q':'What is a FUNCTION','A':'A “chunk” of code that you can call'},
                     {'Q':'What is a CLASS','A':'A template of functions and variables in an object'},
                     {'Q':'What is an OBJECT','A':'An entity having a specific identity, specific characteristics and specific behavior'},
                     {'Q':'What is a MODULE','A':'A file with code you can import and use again'},]

    answerList = []
    for item in questionList:
        answerList.append(item['A'])

    return questionList,answerList

def getQuestion(q,answerList):
    question_text = q['Q']
    answer_text = q['A']
    answer_option = []
    answer_option.append(answer_text)
    while len(answer_option) < 4:
        newItem = random.choice(answerList)
        if newItem not in answer_option:
            answer_option.append(newItem)
    random.shuffle(answer_option)
    print(f'QUESTION: {question_text}')
    print('-'*20)
    i=1
    for item in answer_option:
        print(f'{i}: {item}')
        i+=1
    print('\n')
    return answer_text,answer_option,question_text


def getPlayerAnswer(answer_option):
    print('Write your answer:')
    player_answer = input()
    if player_answer.isnumeric() == True:
        try:
            player_answer = answer_option[int(player_answer)-1]
        except:
            pass
    return player_answer

def startQuizz():
    question_list,answerList = getQuestionList()
    question_num = 0
    answer_text = ''
    question_text = ''
    answer_option = []
    player_wrong_answer=[]
    points = 0
    random.shuffle(question_list)
    print('\n- DATA TYPE QUIZ -\n')
    input('To START Press "ENTER"')
    print('\n')
    for q in question_list:
        print('='*20)
        print(f'QUESTION {question_num+1}/{len(question_list)}\n')
        answer_text,answer_option,question_text = getQuestion(q,answerList)
        player_answer = getPlayerAnswer(answer_option)
        if player_answer.lower() == answer_text.lower():
            print('CORRECT')
            points += 1
        else:
            player_wrong_answer.append([player_answer,answer_text,question_text])
            print(f'WRONG \n Answer = {answer_text}\n ---------------------- \n You Answered {player_answer}')
        input(f'Press "ENTER" for NEXT\n\n')
        question_num += 1
    endQuizz(points,question_num,player_wrong_answer)


def endQuizz(points,totalPoints,player_wrong_answer):
    print('='*20)
    print('YOU HAVE COMPLEATED THE QUIZ\n')
    print('-'*5)
    print(f'POINTS: {points}/{totalPoints}')
    print('-'*5)
    print('YOUR WRONG ANSWER:')
    print('\n')
    for items in player_wrong_answer:
        print(f'QUESTION: {items[2]}')
        print(f'YOUR ANSWER: {items[0]}')
        print(f'CORRECT: {items[1]}')
        print('-'*5)
    print('='*20)
    print('\nDo you want to replay (Y/N):')
    x = input()
    if x.lower() == 'y':
        print('RESTARTING')
        print('\n'*3)
        startQuizz()
    else:
        print('END')

startQuizz()
