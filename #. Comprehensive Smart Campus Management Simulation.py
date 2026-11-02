students = []
while True:
    print("\n1.Add 2.View 3.Attendance 4.Marks 5.Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        students.append([input("Name: "), input("Roll: "), 0, 0])
    elif ch == "2":
        for s in students: print(s)
    elif ch == "3":
        for s in students: s[2] += 1
    elif ch == "4":
        for s in students: s[3] = int(input("Marks: "))
    elif ch == "5": break
    