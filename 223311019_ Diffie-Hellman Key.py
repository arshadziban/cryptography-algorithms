p = int(input("Enter prime number: "))
g = int(input("Enter generator: "))

a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

KA = pow(B, a, p)
KB = pow(A, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)

print("Alice Secret Key:", KA)
print("Bob Secret Key:", KB)

if KA == KB:
    print("Shared Secret Key Matched")
else:
    print("Key Not Matched")