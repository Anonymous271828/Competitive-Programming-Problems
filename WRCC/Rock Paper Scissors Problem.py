a = 0
b = 0
rounds_won_a = 0
rounds_won_b = 0
for i in range(int(input())):
    for j in range(5):
        answers = input().split(" ")
        if answers[0] == "R" and answers[1] == "S":
            a = a + 1
        elif answers[0] == "R" and answers[1] == "P":
            b = b + 1
        elif answers[0] == "P" and answers[1] == "S":
            b = b + 1
        elif answers[0] == "S" and answers[1] == "R":
            b = b + 1
        elif answers[0] == "P" and answers[1] == "R":
            a = a + 1
        elif answers[0] == "S" and answers[1] == "P":
            a = a + 1
    if a > b:
        rounds_won_a = rounds_won_a + 1
    elif b > a:
        rounds_won_b = rounds_won_b + 1
    a = 0
    b = 0

winner = max([rounds_won_a, rounds_won_b])
if rounds_won_a == rounds_won_b:
    print("TIE")
elif [rounds_won_a,rounds_won_b].index(winner) == 0:
    print("A", winner - min([rounds_won_a, rounds_won_b]))
else:
    print("B", winner - min([rounds_won_a, rounds_won_b]))