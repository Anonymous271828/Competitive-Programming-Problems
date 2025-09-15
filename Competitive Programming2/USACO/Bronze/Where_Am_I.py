# Sep. 12th, 2025
# By: Sol Kwak
# Description: sets and maps
# Time Complexity: O(n)
# Additional comments: pretty easy if you plan ahead. lowk chatgpt kinda carried here and gave me an introductory hint
# that got the cobwebs out of my head. they're back in now though, dw

file = open("whereami.in")
n = int(file.readline())
main_string = file.readline()

for k in range(n):
    substrings = set()
    for i in range(n-k+1):
        substrings.add(main_string[i:i+k])
    if len(substrings) == n-k+1:
        print(k, file=open("whereami.out", "w"))
        break