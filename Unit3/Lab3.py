'''
Frequency Country using Dictionaries
'''
text = input("Enter a sentence: ")

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("\n--- CHARACTER FREQUENCY ---")

for char, count in frequency.items():
    print(char, ":", count)