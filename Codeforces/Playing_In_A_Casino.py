# May 13th, 2025
# By: Sol Kwak
# Description: A permutation solution
# Time Complexity: O(nlog(n))
# Additional comments: not too difficult

repeat = int(input())

for i in range(repeat):
    n, m = filter(int, input())
    cards = []
    for j in range(n):
        cards.append(list(filter(int, input())))
    total = 0
    for a in range(len(cards)-1):
        for b in range(a+1, len(cards)):
            for c in range(m):
                total += abs(cards[a][c] - cards[b][c])
    print(total)
