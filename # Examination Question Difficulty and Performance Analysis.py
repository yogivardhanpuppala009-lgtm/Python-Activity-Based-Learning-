
key = ["A", "B", "C", "D"]
answers = [
    ["A", "B", "C", "A"],
    ["A", "C", "C", "D"],
    ["B", "B", "D", "D"]
]

for i in range(4):
    count = 0

    for student in answers:
        if student[i] == key[i]:
            count += 1

    rate = count / len(answers) * 100

    print("Question", i+1)
    print("Success Rate:", rate, "%")

    if rate >= 75:
        print("Easy")
    elif rate >= 40:
        print("Medium")
    else:
        print("Hard")
