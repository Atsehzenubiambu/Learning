# Task 1: Create a tuple of coordinates and unpack
coordinates = (10, 20)

x, y = coordinates
print("x:", x)
print("y:", y)

# Task 2: Set of numbers
A = {1, 2, 3}
B = {3, 4, 5}
# Union
print(A|B)
# Intersection
print(A&B)
# Difference
print(A-B)

# Task 3: Convert a list with duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique_set = set(numbers)
print(unique_set)