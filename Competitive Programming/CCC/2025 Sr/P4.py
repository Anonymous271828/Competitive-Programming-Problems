N, M = map(int, input().split(" "))
tunnels = {}
for i in range(M):
    a, b, c = map(int, input().split(" "))
    a -= 1
    b -= 1
    if a not in tunnels:
        tunnels[a] = [(b, c)]
    else:
        tunnels[a].append((b, c))

    if b not in tunnels:
        tunnels[b] = [(a, c)]
    else:
        tunnels[b].append((a, c))


final = []
print(tunnels)

def res(room, d, c):
    if room == N-1:
        final.append(d)
    else:
        for i in range(len(tunnels[room])):
            res(tunnels[room][i][0], d + abs(c - tunnels[room][i][1]), tunnels[room][i][1])


res(0, 0, 0)
print(min(final))