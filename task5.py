# Get list of words from user
words = []
while True:
    word = input("Enter a word (or 'done' to finish): ")
    if word.lower() == 'done':
        break
    words.append(word)

# Create new list with words of odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print results
print("\nOriginal words:", words)
print("Words with odd number of characters:", odd_length_words)

input("\nPress Enter to exit...")