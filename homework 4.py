""" a = input()leng = 0
b = 1a = a.replace('h', '!')
for i in range(len(a) - 1):    if a[i] == a[i + 1]:
        b += 1        leng = max(leng, b)
    else:        p = 1
print(leng, st) """
"""a = input()b = a[a.find('(') + 1 : a.find(')')]
print(b)"""