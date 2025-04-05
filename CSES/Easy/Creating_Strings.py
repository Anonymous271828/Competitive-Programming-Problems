# Feb. 17th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n!)
# Additional comments: definitely the most jank solution; can probably be improved in terms of both speed and memory;
# but i'm lazy. also, i just took a fat nap, so let me warm my brain up. this problem took me like an hour.
val = input()
ll = {}


def res(char, l, r):
    if l == r:
        v = "".join(char)
        if v not in ll:
            ll["".join(char)] = 0
    else:
        for i in range(l, r):
            char[i], char[l] = char[l], char[i]
            res(char, l+1, r)
            char[l], char[i] = char[i], char[l]


res(sorted(list(val)), 0, len(val))

print(len(ll))
for i in sorted(ll):
    print(i)