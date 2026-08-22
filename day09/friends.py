# Duplicate remover and common friends finder
friends1 = ["Rahim", "Favour", "Nessa", "Zennie", "Gizzy"]
friends2 = ["Nazzy", "Zennie", "Franky", "Rahim", "Favour"]

unique1 = set(friends1)
unique2 = set(friends2)

mutual_friends  = unique1 & unique2

print("Unique friends of person 1:", unique1)
print("Unique friends of person 2:", unique2)
print("Mutual friends:", mutual_friends)