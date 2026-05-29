marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Eligible for admission")
    else:
        print("Age criteria not met")
else:
    print("Marks criteria not met")