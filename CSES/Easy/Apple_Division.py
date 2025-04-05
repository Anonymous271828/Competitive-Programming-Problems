# Feb. 17th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: O(n!)
# Additional comments: meh problem; not too hard. Finally learned how to think of recursion, was pretty nice.

n = int(input())
l = list(map(int, input().split(" ")))

def res(l1, l2,level):
    if len(l1) + len(l2) != n:
        result1 = res(l1 + [l[level]], l2,level+1)
        result2 = res(l1, l2 + [l[level]],level+1)
        return min(result1, result2)
    else:
        return abs(sum(l1) - sum(l2))

print(res([],[], -1))