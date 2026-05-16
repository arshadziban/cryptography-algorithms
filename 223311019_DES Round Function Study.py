IP = [2,6,3,1,4,8,5,7]
EP = [4,1,2,3,2,3,4,1]

S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

p = "10100011"
k = "10100100"

ip = "".join(p[i-1] for i in IP)
print("Initial Permutation:", ip)

L, R = ip[:4], ip[4:]
print("Left:", L)
print("Right:", R)

ep = "".join(R[i-1] for i in EP)
print("Expansion:", ep)

x = "".join(str(int(ep[i]) ^ int(k[i])) for i in range(8))
print("XOR:", x)

a = x[:4]
r = int(a[0]+a[3],2)
c = int(a[1]+a[2],2)

print("S-Box:", bin(S0[r][c])[2:].zfill(2))