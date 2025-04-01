# Feb. 17th-18th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n! * n)
# Additional comments: not the best, can definitely remove that weird n in the time complexity or the global var; but
# im too lazy. it has already taken me an hour and its 12:43 am, i need to move on.

val = [[],[],[],[],[],[],[],[]]
total = 0
for _ in range(8):
    inpt = input()
    for i in range(8):
        val[i].append(inpt[i])


def diags(l, j, c):
    for a,b in enumerate(l):
        if b == j or abs(b-j) == abs(a-c):
            return False
    else:
        return True

def res(i, c, prev):
    for j in range(8):
        if val[c][j] == "." and diags(prev, j, c):
            if abs(j - i) > 1:
                if c < 7:
                    res(j, c+1, prev + [j])
                else:
                    global total
                    total += 1

res(-2, 0, [])
print(total)