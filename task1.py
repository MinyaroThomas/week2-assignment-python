# Get list of integers from user
numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == 'done':
        break
    try:
        numbers.append(int(num))
    except ValueError:
        print("Please enter a valid integer!")

# Calculate and print sum
total = sum(numbers)
print(f"\nYour numbers: {numbers}")
print(f"Sum of all numbers: {total}")
input("\nPress Enter to exit...")