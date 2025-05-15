import html
import random

import requests


class Question:
    def __init__(self, statement, correct_answer, answers):
        self.statement = statement
        self.correct_answer = correct_answer
        self.answers = answers
        self.correct_answer_index = 0

    def print_question(self):
        print(html.unescape(self.statement))
        for i, answer in enumerate(self.answers, start=1):
            if answer.lower() == self.correct_answer.lower():
                self.correct_answer_index = i
            print(f"- {i}.{html.unescape(answer)}")

    def check_user_answer(self, user_answer):

        print(f"Repesuta usuario: {user_answer}")
        print(f"Valor correcto {self.correct_answer_index}")
        return self.correct_answer_index == user_answer


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


def _obtain_user_response(question_progress):
    user_response = 0
    while user_response < 1 or user_response > len(question_progress.answers):
        question_progress.print_question()
        user_response = input("Selecciona la opción que crea correcta, (Escriba el número de la respuesta): ")
        if user_response.isdigit():
            user_response = int(user_response)
            if user_response < 1 or user_response > len(question_progress.answers):
                print("Por favor ingrese un número que sea válido")
        else:
            user_response = 0
            print("Por favor indique números enteros")
    return user_response


questions = _obtain_questions()
list_questions = _convert_json_question(questions)

points = 0

for question in list_questions:

    response = _obtain_user_response(question)
    if question.check_user_answer(response):
        print("Respuesta correcta")
        points += 1
    else:
        print(f"Incorrecto la repuesta correcta es {question.correct_answer}")
    print(f"Puntuación {points}")
