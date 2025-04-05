numbers=["1","2","3","4","5","6","7","8", "9", "0"]
v = input()
vals = []
letters = []
num = ""
for i in range(0, len(v)):
    if v[i] in numbers:
        num += v[i]
        #print(num)
    else:
        if num != "":
            vals.append(int(num))
            num = ""
        letters.append(v[i])
if num != "":
    vals.append(int(num))
    num = ""
c = int(input())

i = 0
c = c % sum(vals)
while True:
    if c < 0:
        print(letters[i-1])
        break
    elif c == 0:
        print(letters[i])
        break
    else:
        c -= vals[int(i)]
        i = (i + 1) % len(vals)