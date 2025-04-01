# Feb. 14th, 2025
# By: Sol Kwak
# Description: A simulation solution
# Time Complexity: O(n)
# Additional comments: took too long to figure out usaco submitting requirements. Got it eventually though.

file = open("mixmilk.in")

l = [file.readline().split(" ") for _ in range(3)]
val = []
for i in range(100):
    remainder = min(int(l[(i+1)%3][0]), int(l[(i+1)%3][1]) + int(l[i%3][1]))
    l[i % 3][1] = int(l[(i + 1) % 3][1]) + int(l[i % 3][1]) - remainder
    l[(i+1)%3][1] = remainder

print("{}\n{}\n{}".format(l[0][1], l[1][1], l[2][1]), file=open("mixmilk.out", "w"))