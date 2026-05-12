ciphertext = input("enter the ciphertext: ")

ciphertext = ciphertext.upper()

frequency = {}
for i in range(65, 91):
    letter = chr(i)
    frequency[letter] = 0

total_letters = 0
for ch in ciphertext:
    if ch.isalpha():
        frequency[ch] += 1
        total_letters += 1

print("\nletter frequency count")
for letter in frequency:
    print(letter, ":", frequency[letter])

print("\npercentage frequency")
for letter in frequency:
    if total_letters > 0:
        percent = (frequency[letter] / total_letters) * 100
    else:
        percent = 0

    print(letter, ":", format(percent, ".2f"), "%")

sorted_letters = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
print("\ntop 5 most frequent letters")
for i in range(min(5, len(sorted_letters))):
    letter = sorted_letters[i][0]
    count = sorted_letters[i][1]

    print(str(i + 1) + ".", letter, "-", count, "times")