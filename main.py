import re

questions = []

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    i = -1
    for line in f:
        question = re.search(r"^\d.*[:?]$", line) # load question
        if question: questions.append( {"question": question.group()} ); i += 1 # check if it's not None

        answer = re.search(r"^[A-D][)].*[.]$", line) # load answer

        if answer: questions[i].setdefault("options", []).append(answer.group()) # check if it's not None

for question in questions: print(question)