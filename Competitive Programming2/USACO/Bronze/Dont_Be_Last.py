# Sep. 12th, 2025
# By: Sol Kwak
# Description: maps
# Time Complexity: O(2n)
# Additional comments: im tired, but this works. took way too long tho

file = open("notlast.in")
n = int(file.readline())

cows = {"Bessie":0, "Elsie":0, "Daisy":0, "Gertie":0, "Annabelle":0, "Maggie":0, "Henrietta":0}
for i in range(n):
    resp = file.readline().split(" ")
    cows[resp[0]] += int(resp[1])

print(cows)
second_smallest = 99999
second_smallest_name = "Tie"
smallest = min(cows.values())
for j in range(len(cows)):
    i = list(cows.values())[j]
    if i > smallest:
        if second_smallest > i:
            second_smallest = i
            second_smallest_name = list(cows)[j]
        elif second_smallest == i:
            second_smallest_name = "Tie"

print(second_smallest_name, file=open("notlast.out", "w"))