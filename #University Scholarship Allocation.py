n = int(input("Enter students: "))
for i in range(n):
    name = input("Enter name: ")
    m1 = int(input("Subject 1 marks: "))
    m2 = int(input("Subject 2 marks: "))
    m3 = int(input("Subject 3 marks: "))
    m4 = int(input("Subject 4 marks: "))
    m5 = int(input("Subject 5 marks: "))
    avg = (m1+m2+m3+m4+m5)/5
    a = float(input("Attendance: ")); income = int(input("Income: "))
    print(name, "Eligible" if min(m1,m2,m3,m4,m5)>=40 and avg>=75 and a>=75 and income<=500000 else "Not Eligible")