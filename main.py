import random
import re
from termcolor import cprint

questions = []

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    i = -1
    for line in f:
        question = re.search(r"^\d.*[:?]$", line) # load question
        if question: questions.append( {"question": question.group()} ); i += 1 # check if it's not None

        answer = re.search(r"^[A-D][)].*[.]$", line) # load answer

        if answer: questions[i].setdefault("options", []).append(answer.group()) # check if it's not None

for question in questions:
    random.shuffle(question["options"])

    i = 0
    for option in question["options"]:
        if option.startswith("A"): question["correct"] = chr(i + 65)
        i += 1

    question["options"] = [chr(i + 65) + option[1:] for i, option in enumerate(question["options"])]

wrong, correct = {}, 0
for question in questions:
    print("\n" + question["question"])

    for option in question["options"]: print(option)

    guess = input("> ").upper().strip()

    if guess == "STOP": break
    elif guess == question["correct"]: correct += 1
    else:
        wrong[question["question"]] = {
            "right": question["options"][ord(question["correct"]) - 65],
            "wrong": question["options"][ord(guess) - 65]
        }

print(f"Score: {correct}/100")

for key, value in wrong.items():
    print(f"\n{key}\n")
    cprint(value["right"], "green", attrs=["bold"])
    cprint(value["wrong"], "red", attrs=["bold"])