import random
import re
from termcolor import cprint

questions = []

# FIND QUESTIONS AND THEIR POSSIBLE ANSWERS
with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    i = -1
    for line in f:
        if question := re.search(r"^\d.*[:?]$", line):
            questions.append( {"question": question.group()} )
            i += 1
            continue

        if answer := re.search(r"^[A-D][)].*$", line):
            questions[i].setdefault("options", []).append(answer.group())

# SHUFFLE QUESTIONS AND THEIR ANSWERS
for question in questions:
    random.shuffle(question["options"]) # shuffle answers

    for i, option in enumerate(question["options"]):
        if option.startswith("A"):
            question["correct"] = chr(i + 65) # save correct answer

    # replace current letter with the correct one
    question["options"] = [chr(i + 65) + option[1:] for i, option in enumerate(question["options"])]

random.shuffle(questions)
for i, question in enumerate(questions): # replace current question number with the correct one
    question["question"] = f"{str(i + 1)}) {re.sub(r"^\d+\)\s*", "", question["question"])}"

# USER INPUT
output, end = {}, True
for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)
    while end:
        guess = input("> ").upper().strip()

        if guess in ["STOP", "EXIT"]:
            end = False
        elif guess == question["correct"]:
            output[question["question"]] = {
                "right": question["options"][ord(question["correct"]) - 65],
                "wrong": ""
            }
            break
        elif guess in ["A", "B", "C", "D"]:
            output[question["question"]] = {
                "right": question["options"][ord(question["correct"]) - 65],
                "wrong": question["options"][ord(guess) - 65]
            }
            break
        else:
            print(f"Invalid command '{guess}'")
    if not end:
        break

# PROGRAM OUTPUT
print(f"=============== Score: {len([v for v in output.values() if v["wrong"] == ""])}/{len(output)} ===============")
for key, value in output.items():
    print(f"\n{key}\n")
    cprint(value["right"], "green", attrs=["bold"])
    cprint(value["wrong"], "red", attrs=["bold"])