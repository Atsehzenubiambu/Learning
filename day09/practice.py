# Task 1: Create a tuple of coordinates and unpack
coordinates = (10, 20)

x, y = coordinates
print("x:", x)
print("y:", y)

# Task 2: Set of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Union
print("Union:", set1 | set2)
# Intersection
print("Intersection:", set1 & set2)
# Difference
print("Difference", set1- set2)

# Task 3: Convert a list with duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique_set = set(numbers)
print(unique_set)