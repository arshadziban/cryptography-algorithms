alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = input("Enter plaintext: ").upper()
key = int(input("Enter key (1-25): "))

ciphertext = ""

for ch in plaintext:
    if ch.isalpha():
        index = alphabet.index(ch)
        new_index = (index + key) % 26
        ciphertext += alphabet[new_index]
    else:
        ciphertext += ch

print("\nEncrypted text:", ciphertext)

decrypted_text = ""

for ch in ciphertext:
    if ch.isalpha():
        index = alphabet.index(ch)
        new_index = (index - key) % 26
        decrypted_text += alphabet[new_index]
    else:
        decrypted_text += ch

print("Decrypted text:", decrypted_text)