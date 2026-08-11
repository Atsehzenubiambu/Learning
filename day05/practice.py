#Task 1: Add Positive Negative and Zero Checker
number = float(input("Enter a number:"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Task 2: Grading Script
score = float(input("Enter you score:"))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")