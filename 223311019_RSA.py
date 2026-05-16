from math import gcd

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while gcd(e, phi) != 1:
    e += 1

d = 1
while (d * e) % phi != 1:
    d += 1

m = int(input("Enter message: "))

c = pow(m, e, n)
pt = pow(c, d, n)

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Ciphertext:", c)
print("Decrypted Text:", pt)