# Get first set of numbers
print("Enter numbers for first set (enter 'done' when finished)")
set1 = set()
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break
    try:
        set1.add(int(num))
    except ValueError:
        print("Please enter a valid integer!")

# Get second set of numbers
print("\nEnter numbers for second set (enter 'done' when finished)")
set2 = set()
while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break
    try:
        set2.add(int(num))
    except ValueError:
        print("Please enter a valid integer!")

# Find common elements
common_elements = set1.intersection(set2)

# Print results
print(f"\nFirst set: {set1}")
print(f"Second set: {set2}")
print(f"Common elements: {common_elements}")

input("\nPress Enter to exit...")