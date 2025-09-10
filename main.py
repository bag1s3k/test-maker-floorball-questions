import random
import re

questions = {}

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    for line in f:
        question = re.search(r"^\d.*[:?]$", line)

        if question:
            question = question.group()
            questions[question] = list()
            current_question = question


        answer = re.search(r"^\w[)].*[.]$", line)
        if answer: questions[current_question].append(answer.group())

for k, v in questions.items():
    random.shuffle(questions[k])

for k, v in questions.items():
    print(k + "\n" + "\n".join(v) + "\n")