# Feb. 18th, 2025
# By: Sol Kwak
# Description: recursion brute-force
# Time Complexity: less than O(n! * n)
# Additional comments: bruh, this crap is so bad. it's all school's fault; was locked in during the weekend,
# can't code after going to school.

def res_3(l, r, c, rect_list_x, rect_list_y):
    global something_found
    if not something_found:
        if l == r:
            if len(set(rect_list_x)) == 1:
                if sum(rect_list_y) == rect_list_x[0]:
                    print(rect_list_x[0])
                    something_found = True
            elif len(set(rect_list_y)) == 1:
                if sum(rect_list_x) == rect_list_y[0]:
                    print(rect_list_x[0])
                    something_found = True

            if something_found:
                letter_dict = {0:"A", 1:"B", 2:"C"}
                for i in range(r):
                    for j in range(rect_list_y[i]):
                        print(letter_dict[i]*rect_list_x[i])

            else:
                #print(rect_list_x, rect_list_y)
                if rect_list_x[1] + rect_list_x[2] == rect_list_x[0] and rect_list_y[2] == rect_list_y[1]:
                    if rect_list_x[0] == rect_list_y[0] + rect_list_y[1]:
                        print(rect_list_x[0])
                        something_found = True

                elif rect_list_y[1] + rect_list_y[2] == rect_list_y[0] and rect_list_x[2] == rect_list_x[1]:
                    if rect_list_y[0] == rect_list_x[0] + rect_list_x[1]:
                        print(rect_list_y[0])
                        something_found = True

                if something_found:
                    letter_dict = {0: "A", 1: "B", 2: "C"}
                    for j in range(rect_list_x[0]):
                        print(letter_dict[0] * rect_list_x[0])
                    for j in range(rect_list_y[1]):
                        print(letter_dict[1] * rect_list_x[1] + letter_dict[2] * rect_list_x[2])
        else:
            for i in range(l, r):
                v[i], v[l] = v[l], v[i]
                res_3(l+1, r, 0, [i[c] for i in v], [i[1-c] for i in v])
                res_3(l+1, r, 1, [i[c] for i in v], [i[1-c] for i in v])
                v[l], v[i] = v[i], v[l]
                res_3(l + 1, r, 0, rect_list_x+[v[i][c]], rect_list_y+[v[i][1-c]])
                res_3(l + 1, r, 1, rect_list_x+[v[i][c]], rect_list_y+[v[i][1-c]])


x1, y1, x2, y2, x3, y3 = map(int, input().split(" "))
v = [(x1, y1), (x2, y2), (x3, y3)]
something_found = False

if int((x1*y1 + x2*y2 + x3*y3)**(1/2)) != (x1*y1 + x2*y2 + x3*y3)**(1/2):
    print(-1)
else:
    res_3(0, len(v), 0, [], [])
    res_3(0, len(v), 1, [], [])