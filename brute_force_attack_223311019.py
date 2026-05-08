alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Enter the ciphertext
message = input("Enter the ciphertext (as uppercase): ")

print("\nPossible decryptions:\n")

for key in range(1, 26):
    decrypted_text = ""

    for ch in message:
        if ch.isalpha():
            index = alphabet.index(ch)
            new_index = (index - key) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += ch

    print("Key", key, "->", decrypted_text)