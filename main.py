import random
from termcolor import cprint

questions = {}

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:

    for line in f:
        try:
            line = line.strip()
            if line[0].isdigit():
                key = line
                questions[key] = {
                    "options": list(),
                    "answer": random.randint(0, 3)
                }
            else:
                questions[key]["options"].append(line.strip())
        except:
            continue

for key, value in questions.items():
    possibles_indexes = [0, 1, 2, 3]
    possibles_indexes.remove(value["answer"])
    random.shuffle(possibles_indexes)

    copy_list = list(value["options"])

    copy_list[value["answer"]] = value["options"][0]
    i = 1
    for index in possibles_indexes:
        copy_list[index] = value["options"][i]
        i += 1

    value["options"] = copy_list

    # Correct numbering of answers
    letter = 68
    i = len(value["options"]) - 1
    while i >= 0:
        value["options"][i] = chr(letter) + value["options"][i][1:]

        i -= 1
        letter -= 1


items = list(questions.items())
random.shuffle(items)
questions = dict(items)

i, correct = 1, 0
wrong = {}
for key, value in questions.items():
    key = str(i) + key[2:]

    i += 1
    print("\n" + key + "\n")
    for answer in value["options"]:
        print(answer)

    guess = input("> ").lower()

    if guess == "stop": break
    elif ord(guess) - 97 == value["answer"]: correct += 1
    else: wrong[key] = {
        "right": value["options"][value["answer"]],
        "wrong": value["options"][ord(guess) - 97]
    }

print(f"Score: {correct}/100")

for key, value in wrong.items():
    print(f"\n{key}\n")
    cprint(value["right"], "green", attrs=["bold"])
    cprint(value["wrong"], "red", attrs=["bold"])