x, y, a, b = map(int,input().split(" "))


size1 = 2 * (x + a + max(b, y))
size2 = 2 *(b + y + max(a, x))

print(min(size1, size2))