# Feb. 15th, 2025
# By: CHAT-GPT. NOT SOL KWAK
# Description: apparently this is faster
# Time Complexity: O(n^2)
# Additional comments: i'm too lazy to read whatever chatgpt wrote. i'm just going to test it.
# Problem: Okay it worked. I'll review, then explain it.
# Solution: it's actually really simple. It's just that chatgpt used a hashmap; placed all values into it,
# then, instead of doing an O(n) search, asked the hashmap if hashmap[average_value] exists.

N = int(input())
flowers = list(map(int, input().split()))

# Step 1: Compute prefix sum
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + flowers[i]

total = N  # Each single element is trivially a valid subarray

# Step 2: Check all subarrays using prefix sums
for i in range(N):  # Start index
    for j in range(i + 1, N):  # End index
        subarray_sum = prefix[j + 1] - prefix[i]  # O(1) sum retrieval
        length = j - i + 1
        if subarray_sum % length == 0:  # Check if average is an integer
            avg = subarray_sum // length
            if avg in flowers[i:j+1]:  # O(N) search → Can be optimized with a set
                total += 1

print(total)
