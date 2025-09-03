import random

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

    print(f"Key: {key}\nValue: {value}")
    value["options"] = copy_list
    print(f"Key: {key}\nValue: {value}")

    # Correct numbering of question
    letter = 68
    i = len(value["options"]) - 1
    while i >= 0:
        value["options"][i] = chr(letter) + value["options"][i][1:]

        i -= 1
        letter -= 1

    print(f"Key: {key}\nValue: {value}")
    break