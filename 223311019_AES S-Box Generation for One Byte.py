b = int(input("Enter hex byte: "), 16)

# GF(2^8) Multiplication
def mul(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a <<= 1
        if hi:
            a ^= 0x11B
        b >>= 1
    return p % 256

# Multiplicative Inverse
inv = 0

for i in range(256):
    if mul(b, i) == 1:
        inv = i
        break

# Affine Transformation
s = inv

for i in range(1, 5):
    s ^= ((inv << i) | (inv >> (8-i))) & 0xFF

s ^= 0x63

print("S-Box Value:", hex(s)[2:].upper())