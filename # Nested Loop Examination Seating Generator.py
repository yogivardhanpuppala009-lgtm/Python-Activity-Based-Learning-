rows = 3
cols = 4

for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            print("R", end="  ")
        elif (i + j) % 2 == 0:
            print("T", end="  ")
        else:
            print("B", end="  ")
    print()