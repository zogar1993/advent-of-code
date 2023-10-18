import sys

with open('2022_14.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

rock_lines = [[{"x": int(item[0]), "y": int(item[1])} for item in [item.split(",") for item in line.split(" -> ")]] for line in lines]


min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize

for rock_line in rock_lines:
    for rock in rock_line:
        if rock["x"] > max_x:
            max_x = rock["x"]
        if rock["x"] < min_x:
            min_x = rock["x"]
        if rock["y"] > max_y:
            max_y = rock["y"]
        if rock["y"] < min_y:
            min_y = rock["y"]

x_length = max_x - min_x + 1
y_length = max_y - min_y + 1
for rock_line in rock_lines:
    for rock in rock_line:
        rock["x"] -= min_x
        rock["y"] -= min_y

cave = [[" " for _ in range(x_length)] for _ in range(y_length)]

for rock_line in rock_lines:
    for i in range(len(rock_line) - 1):
        rock_a = rock_line[i]
        rock_b = rock_line[i + 1]

        x_direction = 1 if rock_a["x"] < rock_b["x"] else -1
        y_direction = 1 if rock_a["y"] < rock_b["y"] else -1
        for x in range(rock_a["x"], rock_b["x"] + x_direction, x_direction):
            for y in range(rock_a["y"], rock_b["y"] + y_direction, y_direction):
                cave[y][x] = "#"

for line in cave:
    print(line)

