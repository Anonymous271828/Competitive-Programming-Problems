# Feb. 14th, 2025
# By: Sol Kwak
# Description: A simulation solution
# Time Complexity: O(3n)
# Additional comments: very easy and intuitive, even for really dumb me.

read = open("shell.in")
n = int(read.readline())
ultimate = 0
counter = 0
times_iterated = 0

values = []

for j in range(3):
    total = [0, 0, 0]
    total[j] = 1
    for i in range(n):
        if j < 1:
            a, b, c = [int(i) for i in read.readline().split()]
            values.append([a,b,c])
        a, b, c = values[i]
        total[a-1], total[b-1] = total[b-1], total[a-1]
        
        if total[c - 1] == 1:
            counter += 1
            print(j)
    if ultimate < counter:
        ultimate = counter
    counter = 0
    
print(ultimate, file=open("shell.out", "w"))
