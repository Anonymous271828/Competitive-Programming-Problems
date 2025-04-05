# Feb. 18th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n! * n)
# Additional comments: not fun problem, can probably be optimized. Python is ass for these problems, have to call
# .copy() a bajillion times. i still need practice.

file = open("lineup.in")
cows2 = ["Beatrice", "Bella", "Belinda", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
N = int(file.readline())
restrictions = []
correct = []


for i in range(N):
    d = file.readline().split(" must be milked beside ")
    restrictions.append((d[0], d[1][:-1]))

#print(restrictions)


def res(l, r, cows):
    if l == r:
        for i in restrictions:
            k = cows.index(i[0])
            h = cows.index(i[1])
            if abs(h - k) > 1:
                break
        else:
            correct.append(cows.copy())
    else:
        for i in range(l, r):
            cows[l], cows[i] = cows[i], cows[l]
            #print(cows)
            res(l+1,r, cows)
            cows[i], cows[l] = cows[l], cows[i]

res(0, 8, cows2.copy())
print("\n".join(sorted(correct)[0]), file=open("lineup.out", "w"))