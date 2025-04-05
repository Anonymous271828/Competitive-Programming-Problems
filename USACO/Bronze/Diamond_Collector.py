# Feb. 14th-15th, 2025
# By: Sol Kwak
# Description: A hash-map and sliding-window solution.
# Time Complexity: O(n log n)
# Additional comments: bruh, this took way too long. I should retire.

file = open("diamond.in")
n, k = file.readline().split(' ')
n= int(n)
k = int(k)
v = {}
for _ in range(n):
    i = int(file.readline())
    if i not in v:
        v[i] = 1
    else:
        v[i] += 1

v2 = sorted(v)
a, b = 0, 0

for i in range(len(v2)):
    a = 0
    for j in range(i, len(v2)):
        if abs(v2[j] - v2[i]) > k:
            break
        else:
            a += v[v2[j]]
    b = max(b, a)

print(b, file=open("diamond.out", "w"))