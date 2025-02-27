# 1. Create an empty list
my_list = []
print("1. Empty list:", my_list)

# 2. Append elements
my_list = [10, 20, 30, 40]
print("2. After appending:", my_list)

# 3. Insert value at second position
my_list.insert(1, 15)
print("3. After inserting 15:", my_list)

# 4. Extend list
my_list.extend([50, 60, 70])
print("4. After extending:", my_list)

# 5. Remove last element
my_list.pop()
print("5. After removing last element:", my_list)

# 6. Sort in ascending order
my_list.sort()
print("6. After sorting:", my_list)

# 7. Find index of value 30
index_of_30 = my_list.index(30)
print("7. Index of 30:", index_of_30)

input("\nPress Enter to exit...")