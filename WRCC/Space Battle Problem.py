import math
requirements = list(map(int, input().split(" ")))
ships = []

for i in range(requirements[0]):
    enemy_ship = list(map(int, input().split(" ")))
    enemy_ship[0] = requirements[3] * math.ceil((enemy_ship[0] - requirements[2])/ requirements[2])
    enemy_ship.append(enemy_ship)
    enemy_ship[1] = enemy_ship[1] * math.floor(enemy_ship[0] / enemy_ship[2]) + enemy_ship[1]
    enemy_ship.pop(len(enemy_ship) - 1)
    enemy_ship.pop(0)
    #print(enemy_ship)
    ships.append(enemy_ship)
    #print(enemy_ship)
ships_destroyed = 0
for i in sorted(ships):
    #print(i)
    if requirements[1] - i[0] >= 0:
        ships_destroyed = ships_destroyed + 1
        requirements[1] = requirements[1] - i[0]
    else:
        print(ships_destroyed)
        break
else:
    print(len(ships))