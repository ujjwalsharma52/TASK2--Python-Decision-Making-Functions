salary = int(input("Enter salary: "))
experience = int(input("Enter years of experience: "))

if salary >= 30000:
    if experience >= 5:
        print("Eligible for bonus")
    else:
        print("Not enough experience")
else:
    print("Salary criteria not met")