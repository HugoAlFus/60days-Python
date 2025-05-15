import random
import html
import requests


class Question:
    def __init__(self, statement, correct_answer, answers):
        self.statement = statement
        self.correct_answer = correct_answer
        self.answers = answers

    def print_question(self):
        print(html.unescape(self.statement))
        for answer in self.answers:
            print(f"- {answer}")
        print("Selecciona la opción que crea correcta, (Escriba la respuesta tal y como se muestra): ")

    def check_user_answer(self, user_answer):
        return user_answer.casefold() == self.correct_answer.casefold()


URL = "https://opentdb.com/api.php?amount=10"

HEADERS = {
    "Accept": "application/json"
}


def _obtain_questions():
    response = requests.get(URL, headers=HEADERS)
    questions = response.json()
    return questions


def _convert_json_question(questions):
    list_questions = []
    for line in questions["results"]:
        statement = line["question"]
        correct_answer = line["correct_answer"]
        incorrect_answers = line["incorrect_answers"]
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)
        question = Question(statement, correct_answer, answers)
        list_questions.append(question)

    return list_questions


questions = _obtain_questions()
list_questions = _convert_json_question(questions)
points = 0
for question in list_questions:
    question.print_question()
    response = input()
    if question.check_user_answer(response):
        print("Respuesta correcta")
        points += 1
    else:
        print(f"Incorrecto la repuesta correcta es {question.correct_answer}")
    print(f"Puntuación {points}")