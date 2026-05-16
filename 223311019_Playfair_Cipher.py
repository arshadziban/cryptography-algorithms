key = input("Enter key: ").upper().replace("J", "I")
text = input("Enter text: ").upper().replace("J", "I")

# Create Matrix
s = ""

for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in s and ch.isalpha():
        s += ch

mat = [s[i:i+5] for i in range(0, 25, 5)]

print("\nMatrix:")
for row in mat:
    print(row)

# Prepare Plaintext
p = ""
i = 0

while i < len(text):
    a = text[i]

    if i + 1 < len(text):
        b = text[i+1]

        if a == b:
            p += a + "X"
            i += 1
        else:
            p += a + b
            i += 2
    else:
        p += a + "X"
        i += 1

print("\nPrepared Text:", p)

# Find Position
def pos(ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j

# Encryption
cipher = ""

for i in range(0, len(p), 2):
    a, b = p[i], p[i+1]

    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2:
        cipher += mat[r1][(c1+1)%5]
        cipher += mat[r2][(c2+1)%5]

    elif c1 == c2:
        cipher += mat[(r1+1)%5][c1]
        cipher += mat[(r2+1)%5][c2]

    else:
        cipher += mat[r1][c2]
        cipher += mat[r2][c1]

print("\nEncrypted Text:", cipher)

# Decryption
plain = ""

for i in range(0, len(cipher), 2):
    a, b = cipher[i], cipher[i+1]

    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2:
        plain += mat[r1][(c1-1)%5]
        plain += mat[r2][(c2-1)%5]

    elif c1 == c2:
        plain += mat[(r1-1)%5][c1]
        plain += mat[(r2-1)%5][c2]

    else:
        plain += mat[r1][c2]
        plain += mat[r2][c1]

print("Decrypted Text:", plain)