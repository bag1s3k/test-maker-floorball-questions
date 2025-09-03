questions = {}

with open("zasobnik_otazek.txt", "r", encoding="utf-8") as f:
    for line in f:
        try:
            line = line.strip()
            if line[0].isdigit():
                key = line
                questions[key] = list()
            else:
                questions[key].append(line.strip())
        except:
            continue

for key, value in questions.items():
    print(f"Key: {key}\nValue: {value}")