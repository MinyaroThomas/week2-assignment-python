# Create dictionary to store person information
person = {}

# Get user input
person['name'] = input("Enter name: ")
person['age'] = input("Enter age: ")
person['favorite_color'] = input("Enter favorite color: ")

# Print the dictionary
print("\nPerson Information:")
for key, value in person.items():
    print(f"{key}: {value}")

input("\nPress Enter to exit...")