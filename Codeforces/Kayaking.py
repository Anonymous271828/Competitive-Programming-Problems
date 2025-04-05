n = int(input())
v = list(map(int, input().split(" ")))
v.sort()
m = []
lowest = float("inf")
def res(l, r, v):
    if l == r:
        global lowest
        lowest = min(test(0, v), lowest)
    else:
        for i in range(l, r):
            v[l], v[i] = v[i], v[l]
            res(l+1, r, v)
            v[i], v[l] = v[l], v[i]
def test(total, v):
    for i in range(0, len(v), 2):
        print(abs(v[i] - v[i+1]))
        m.append(abs(v[i] - v[i+1]))
        total += abs(v[i] - v[i+1])
    return total

res(0, len(v), v.copy())
print(lowest)