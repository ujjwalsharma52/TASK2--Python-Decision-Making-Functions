marks = int(input("Enter marks: "))
sports = input("Sports quota (yes/no): ")

if marks >= 85 or sports == "yes":
    print("Eligible for scholarship")
else:
    print("Not eligible")