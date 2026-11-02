locations = ["College", "Hospital", "Hostel"]

for place in locations:
    received = int(input("Enter received stock: "))
    distributed = int(input("Enter distributed stock: "))
    damaged = int(input("Enter damaged stock: "))

    remaining = received - distributed - damaged
    print("\nLocation:", place)
    print("Remaining Stock:", remaining)

    if remaining < 20:
        print("Replenishment Required")
    else:
        print("Stock Available")