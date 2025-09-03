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
                    "answer": "1000"
                }
            else:
                questions[key]["options"].append(line.strip())
        except:
            continue

# for key, value in questions.items():
#     print(f"Key: {key}\nValue: {bin(value)}")

for key, value in questions.items():
    to_shuffle = list(str(value["answer"]))

    random.shuffle(to_shuffle)

    value["answer"] = "".join(to_shuffle)


    # letter = 68
    # i = len(value) - 1
    # while i >= 0:
    #     value[i] = chr(letter) + value[i][1:]
    #
    #     i -= 1
    #     letter -= 1
    # print(f"Key: {key}\nValue: {value}")