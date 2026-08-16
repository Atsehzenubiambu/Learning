# Task 1: Print 1-20 using for AND while
# Task 1 a: Using for loop
print("Using for loop:")
for number in range(21):
    print(number)

# Task 1 b: Using while loop
print("Using while loop")
number = 1
while number <= 20:
    print(number)
    number+=1

# Task 2: Multiples of 3
for number in range (1, 101):
    if number % 3 != 0:
        continue
    print(number)

