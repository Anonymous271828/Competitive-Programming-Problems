import numpy as np
requirements = input().split(" ")
total_amount_of_slices = 0
for i in range(int(requirements[0])):
    total_amount_of_slices = total_amount_of_slices + int(input().split(" ")[0])
a = np.ceil(total_amount_of_slices / (int(requirements[1]) * int(requirements[2])))
print(int(requirements[3]) * a)