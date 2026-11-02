capacity = 50
passengers = 0

for i in range(3):
    board = int(input("Enter boarding: "))
    exit = int(input("Enter alighting: "))
    passengers = passengers + board - exit
    print("Passengers:", passengers)

    if passengers > capacity:
        print("Capacity Exceeded")
    else:
        print("Within Capacity")