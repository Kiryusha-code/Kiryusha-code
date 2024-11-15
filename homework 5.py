"""import math
x = input().split()y = input().split()
z = input().split()def corner(m):
    a = math.acos(float(m[0])/math.sqrt(float(m[0])  2 + float(m[1])  2))    return a
b = min(corner(x), corner(y), corner(z))q, w, e = corner(x), corner(y), corner(z)
if q==b:    print(x)
elif w==b:    print(y)
else:    print(z)"""

def simple(n):    a = 0
    for i in range(2, n):        if n % i == 0:
            a += 1    if a == 0:
        return True
    else:        return False
    n = int(input())
for i in range(2, n + 1):    if simple(i):
if str(i) == str(i)[::-1]:            print(i, end=' ')