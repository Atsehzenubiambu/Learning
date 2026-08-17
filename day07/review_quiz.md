# Day 7: Week 1 Review quiz
## 1. Variables
What is a variable in python? Give an example.

Answer: A variable is name used to store a value in Python.
Example:
name = "Python"


## 2. Data Types
What data type is each of these? 
25
3.14
"Python"
True

Answer:
25 is an interger(int)
3.14 is a float(float)
"Python" is a string(str)
True is a boolean(bool)


## 3. Type Conversion
What does this code do?
age = int("25")

Answer: It converts the string "25" into an integer and stores it in the variable age.


## 4. Operators
What is the difference between / and //?

Answer: / is division and returns a float .
       // is floor division and returns the division result without the decimal part.


## 5. Comparison
What is the difference between = and ==?

Answer: = is used to assign a value to a variable while
        == is used to compare to compare two values and check if they are equal.


## 6. Strings
What does this produce?
word = "Python"
print(word[:3])

Answer: Pyt


## 7. Conditionals
What is the purpose of if, elif and else?

Answer:
if checks a condition.
elif checks another condition if the previous condition was false.
else runs when none of the previous conditions are true.


## 8. Loops
What numbers does this produce?
for number in range(2, 10, 2)
print(number)

Answer: 2, 4, 6, 8


## 9. Break vs Condition
What is the differnce between break and continue?

Answer: 
break completely stops the loop.
Continue skips the current iteration and moves to the next iteration.


## 10. Ternary
Write a ternary expression that prints "Even" if a number is even and "Odd" otherwise

Answer:
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)