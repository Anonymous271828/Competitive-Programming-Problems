# Sep. 15th, 2025
# By: Sol Kwak
# Description: greedy
# Time Complexity: O(n)
# Additional comments: easy

file = open("breedflip.in")
n = int(file.readline())

a=file.readline()
b=file.readline()

counter = 0
substring_counter = 0
for i in range(n):
    if a[i] != b[i]:
        counter += 1
    else:
        if counter > 0:
            substring_counter += 1
            counter = 0

print(substring_counter, file=open("breedflip.out", "w"))