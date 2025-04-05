# Feb. 16th-17th, 2025
# By: Sol Kwak
# Description: brute-force
# Time Complexity: less than O(n^3)
# Additional comments: VERY FUN problem, super locked-in. Code took less than 3 minutes, but prep took perhaps
# half an hour. Should definitely start doing this in the future; making a plan, then coding it.

file = open("circlecross.in")
circle = file.readline()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

final = 0
for i in alphabet:
    pos = circle.index(i)
    pos2 = circle[pos+1:].index(i) + pos + 1
    letter_dict = {}
    tots = 0
    for j in circle[pos+1:pos2]:
        if j not in letter_dict:
            letter_dict[j] = 1
        else:
            letter_dict[j] += 1
    for m in list(letter_dict):
        if letter_dict[m] == 1:
            tots += 1

    final += tots

print(int(final/2), file=open("circlecross.out", "w"))