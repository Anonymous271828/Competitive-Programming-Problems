# Feb. 18th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n! * n)
# Additional comments: fun problem, probably more efficient solution. will check when i have internet
# took an hour and a half.

class Restriction:
    def __init__(self, a, b, p, m):
        self.a = a
        self.b = b
        self.p = p
        self.m = m


stalls = {}
restrictions = []
N, M = map(int, input().split(" "))
for i in range(N):
    k = list(map(int, input().split(" ")))
    for j in range(k[0], k[1]+1):
        if j not in stalls:
            stalls[j] = k[2]
        else:
            stalls[j] += k[2]

for i in range(M):
    k = list(map(int, input().split(" ")))
    restrictions.append(Restriction(k[0], k[1], k[2], k[3]))

lowest = float("inf")

def res(l, r, v):
    if l != r:
        for i in range(l, r):
            calc(v + [restrictions[i]])
            res(i+1, r, v + [restrictions[i]])

def calc(v):
    t= 0
    stalls2 = stalls.copy()
    for i in v:
        for j in range(i.a, i.b+1):
            if j in stalls2:
                stalls2[j] -= i.p
        t += i.m

    for i in stalls2:
        if stalls2[i] > 0:
            break
    else:
        global lowest
        lowest = min(t, lowest)


res(0, M, [])
print(lowest)