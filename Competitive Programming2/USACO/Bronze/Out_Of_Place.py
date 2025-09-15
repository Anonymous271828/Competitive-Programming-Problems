# Sep. 15th, 2025
# By: Sol Kwak
# Description: greedy
# Time Complexity: O(n*log(n) + 2n)
# Additional comments: took way to long, holy shit.

file = open("outofplace.in")
n = int(file.readline())
lineup = [int(file.readline()) for _ in range(n)]

sorted_lineup = sorted(lineup)
bessie = None
for i in range(n):
    if lineup[i] != sorted_lineup[i]:
        bessie = (lineup[i], i)
        break

if bessie:
    print(sum(1 for i in range(n) if lineup[i] != sorted_lineup[i])-1, file=open("outofplace.out", "w"))
else:
    print(0, file=open("outofplace.out", "w"))