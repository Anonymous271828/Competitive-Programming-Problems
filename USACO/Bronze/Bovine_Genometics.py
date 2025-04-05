# Feb. 16th, 2025
# By: Sol Kwak
# Description: brute-force
# Time Complexity: less than O(n^3)
# Additional comments: i should start a story about bessie and why she only appears in a few problems.
# might be interesting for future sol. Regardless, pretty easy, took only half an hour. You can also optimize
# memory usage

file = open("cownomics.in")
N, M = map(int, file.readline().split(" "))
good_column = []

for i in range(M):
    good_column.append({"S"})

for i in range(N):
    #good_map.append(file.readline())
    val = file.readline()
    for j in range(M):
        good_column[j].add(val[j])

illegals = []

for i in range(N):
    val = file.readline()
    for j in range(M):
        if val[j] in good_column[j] and j not in illegals:
            illegals.append(j)

print(good_column, illegals)

print(M - len(illegals), file=open("cownomics.out", "w"))