# Feb. 17th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n!)
# Additional comments: saw this in CPH. Thought it was easy at first; let's see how it is.
# Additional comments 2: took 20 minutes; not my proudest moment. definitely need to practice recursion a billion
# times more. i'm so cooked for the ccc; let's just go for honour roll.

s = list(map(int, list(input())))


def res(l, r, v):
    if l != r:
        for i in range(l, r):
            print(v+[s[i]])
            res(i+1, r, v + [s[i]])


res(0, len(s), [])