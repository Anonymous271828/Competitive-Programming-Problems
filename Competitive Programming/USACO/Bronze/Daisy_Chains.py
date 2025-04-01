# Feb. 15th, 2025
# By: Sol Kwak
# Description: brute-force
# Time Complexity: O(n^3) <<< insert skull emoji here. i'm so cooked.
# Additional comments: bro, this has already taken half an hour. kill meeeeee

N = int(input())
flowers = list(map(int, input().split(' ')))

total = [N][0]
av_flowers = 0
for i in range(1, N):
    for j in range(N-i):
        av_flowers = flowers[j:j+i+1]
        if sum(av_flowers)/(i+1) in av_flowers:
            #print(total, i, j)
            total += 1

print(total)