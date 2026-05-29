age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))

if age >= 21 and income >= 25000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")