# Feb. 14th, 2025
# By: Sol Kwak
# Description: A brute-force solution
# Time Complexity: O(n^2)
# Additional comments: very easy and intuitive, even for really dumb me.

n = int(input())
l1 = list(map(int, input().split(" ")))
l2 = list(map(int, input().split(" ")))
max_dist = 0
for i in range(n):
    for j in range(n):
        max_dist = max(max_dist, (l1[i]-l1[j])**2 + (l2[i]-l2[j])**2)
print(max_dist)