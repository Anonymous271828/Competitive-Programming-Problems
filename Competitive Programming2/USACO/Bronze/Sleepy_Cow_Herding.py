# Sep. 15th, 2025
# By: Sol Kwak
# Description: case-work
# Time Complexity: O(1)
# Additional comments: very easy

file = open("herding.in")
final = sorted(list(map(int, file.readline().split(" "))))
n1, n2, n3 = final[0], final[1], final[2]
if n2-n1 == 1 and n3-n2 == 1:
    output= "0"
elif n2 - n1 == 2 or n3 - n2 == 2:
    output = "1"
else:
    output = "2"

if n3 - n2 > n2 - n1:
    output = output + "\n{}".format(n3 - n2 - 1)
else:
    output = output + "\n{}".format(n2 - n1 - 1)
print(output, file=open("herding.out", "w"))