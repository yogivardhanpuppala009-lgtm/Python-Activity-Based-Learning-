candidates = []
n = int(input("Enter number of candidates: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    score = int(input("Enter assessment score: "))
    attendance = int(input("Enter attendance: "))
    if marks >= 60 and score >= 50 and attendance >= 75:
        candidates.append((name, marks + score, attendance))
candidates.sort(key=lambda x: (-x[1], -x[2], x[0]))
print("Internship Ranking:")
for i, c in enumerate(candidates, 1): print(i, c)