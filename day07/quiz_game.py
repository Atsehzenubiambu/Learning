questions = [
    {
        "question": "What is the correct file extension for Python files?", "answer":".py"
    },
    {
        "question": "What function is used to display something in Python?", "answer": "print"
    },
    {
        "question": "What data type is 10?", "answer": "int"
    },
    {
        "question": "What operator is used for floor division?", "answer": "//"
    },
    {
        "question": "What keyword is used to create a condition?", "answer": "if"
    }
]

score = 0

for item in questions:
    print(item["question"])

    user_answer = input("Your answer: ")

    if user_answer.lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! You have one more chance.")

        retry = input("Try again: ")

        if retry.lower() == item["answer"].lower():
            print("Correct on your second try!")
            score += 1
        else:
            print("Wrong again!")

print(f"\nYour final score is {score}/5.")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
