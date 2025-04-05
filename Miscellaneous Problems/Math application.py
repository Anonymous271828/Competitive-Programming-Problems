for q in range(20):
    for d in range(20):
        for n in range(20):
            for p in range(20):
                if q + d + n + p == 0 or q + d + n + p - 1 == 0:
                    pass
                else:
                    number1 = (0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p) / (q + d + n + p)
                    number2 = (0.25 * q + 0.1 * d + 0.05 * n + 0.01 * (p - 1)) / (q + d + n + p - 1)
                    if number1 == 0.17 and number2 == 0.18:
                        print("There are {} nickels".format(n))
print(float("0.5"))
