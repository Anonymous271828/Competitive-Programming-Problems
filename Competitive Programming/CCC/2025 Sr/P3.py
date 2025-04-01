N, M, Q = map(int, input().split(" "))
pens = {}
pens_list = []
for i in range(N):
    f = list(map(int, input().split(" ")))
    pens_list.append(f)
    if f[0] not in pens:
        pens[f[0]] = [f[1]]
    else:
        pens[f[0]].append(f[1])


def calc(pens2):
    total = 0
    biggest = 0
    smallest = float("inf")
    print(pens2)
    for i in pens2:
        pens2[i].sort()
        if len(pens2[i]) > 0:
            total += pens2[i][-1]
            smallest = min(pens2[i][-1], smallest)
        if len(pens2[i]) >= 2:
            biggest = max(biggest, pens2[i][-2])

    if smallest < biggest:
        total = total - smallest + biggest
    print(total)

def main(pens2):
    f = list(map(int, input().split(" ")))
    get_pen = pens_list[f[1]-1]
    if f[0] == 1:
        pens2[get_pen[0]].remove(get_pen[1])
        pens2[f[2]].append(get_pen[1])
        #pens2[f[2]].sort()
    else:
        #print(pens2, f)
        pens2[get_pen[0]].remove(get_pen[1])
        pens2[get_pen[0]].append(f[2])
        #pens2[get_pen[0]].sort()
    calc(pens2)


calc(pens)
for i in range(Q):
    #print(pens)
    main(pens.copy())
    #print(pens)