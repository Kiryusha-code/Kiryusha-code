import random
"""n = random.randint(2, 51)m = random.randint(2, 51)
arr = []for i in range(n):
    brr = []    for j in range(m):
        brr.append(random.randint(1, 51))    arr.append(brr)
mn = 9999999999999999999999999999mx = -9999999999999999999999999999
for i in range(n):    sum = 0
    for j in range(m):        sum += arr[i][j]
    if sum > mx:        mx = sum
        i_mx = i    if sum < mn:
        mn = sum        i_mn = i
print(mn, arr[i_mn])print(mx, arr[i_mx]) """
n = random.randint(2, 51)
m = random.randint(2, 51)arr = []
for i in range(n):    brr = []
    for j in range(m):        brr.append(random.randint(-50, 51))
    arr.append(brr)for i in range(n):
    print(arr[i])for i in range(n):
    for j in range(m):        arr[i][j] = (arr[i][j]) % 2
for i in range(n):    print(arr[i])