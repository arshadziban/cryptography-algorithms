alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substitution_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
encrypt_table = {}
decrypt_table = {}
for i in range(26):
    encrypt_table[alphabet[i]] = substitution_key[i]
    decrypt_table[substitution_key[i]] = alphabet[i]

print("substitution table")

for letter in alphabet:
    print(letter, "->", encrypt_table[letter])

plaintext = input("\nenter plaintext: ")

plaintext = plaintext.upper()

ciphertext = ""

for ch in plaintext:
    if ch.isalpha():
        ciphertext += encrypt_table[ch]
    else:
        ciphertext += ch

print("\nencrypted text:", ciphertext)

decrypted_text = ""

for ch in ciphertext:
    if ch.isalpha():
        decrypted_text += decrypt_table[ch]
    else:
        decrypted_text += ch

print("decrypted text:", decrypted_text)