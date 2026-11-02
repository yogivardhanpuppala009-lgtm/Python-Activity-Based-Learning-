email = input("Enter student email: ")
reg = input("Enter registration ID: ")

if "@" in email and "." in email and email.count("@") == 1:
    print("Valid Email")
else:
    print("Invalid Email")

if len(reg) >= 5 and reg.isalnum():
    print("Valid Registration ID")
else:
    print("Invalid Registration ID")