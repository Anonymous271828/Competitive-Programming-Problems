#Sep. 12th, 2025
# By: Sol Kwak
# Description: lowkey, this was done before sep. 12 but idk when. idk
# Time Complexity: O(n) i think
# Additional comments: i don't remember doing this

values_dict = {}
for i in range(int(input())):
    line_list = list(map(int, input().split(" ")))
    #print(line_list)
    if line_list[0] == 0:
        values_dict[line_list[1]] = line_list[2]
        #print(values_dict)
    else:
        if line_list[1] in values_dict:
            print(values_dict[line_list[1]])
        else:
            print(0)