# Feb. 16th, 2025
# By: Sol Kwak
# Description: brute-force
# Time Complexity: less than O(n^3)
# Additional comments: took half an hour, not too bad. Definitely can be optimized though.

file = open("gymnastics.in")

K, N = map(int, file.readline().split(" "))
pracs = {}
for i in range(1, N + 1):
    pracs[i] = []
for _ in range(K):
    v = list(map(int, file.readline().split(" ")))
    print(v)
    for i in range(N):
        pracs[v[i]].append(i)

final = 0
for i in range(N):
    for j in range(N):
        if i != j:
            for a in range(K):
                if pracs[i+1][a] < pracs[j+1][a]:
                    break
            else:
                final += 1

print(final, file=open("gymnastics.out", "w"))