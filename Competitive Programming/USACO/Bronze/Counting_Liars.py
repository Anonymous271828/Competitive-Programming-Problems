# Feb. 15th-16th, 2025
# By: Sol Kwak
# Description: brute-force
# Time Complexity: O(n^2)
# Additional comments: damn, tried to cheat it. didn't work :(.
# Additional comments 2: Restarted.
# Additional comments 3: Restarted again. Took a break. Damn, has taken too long already. Probably 3 hours on this
# problem :(
# Additional comments 4: if you have some difficulty understanding it, especially if l and g are at the same point,
# the boundary will still work, because it analyzes the situation as if the point was an option.

N = int(input())
l = []
g = []
for i in range(N):
    put = input().split(" ")
    if put[0] == "L":
        l.append(int(put[1]))
    else:
        g.append(int(put[1]))

l.sort()
g.sort()

possible = sorted(set(g + l))

liars = float('inf')
for i in possible:
    current_liars = 0
    for j in g:
        if j > i:
            current_liars += 1
    for j in l:
        if j < i:
            current_liars += 1
    liars = min(liars, current_liars)

print(liars)