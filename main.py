questions = {}

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    i = 0
    for line in f:
        if line[0].isalnum():
            try:
                if line[0].isdigit():
                    key = line.strip()
                    questions[key] = list()
                else:
                    questions[key].append(line.strip())
            except:
                continue

for key, value in questions.items():
    print(f"Key: {key}\nValue: {value}")