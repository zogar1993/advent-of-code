import sys

with open('2022_14.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

rock_lines = [[{"x": int(item[0]), "y": int(item[1])} for item in [item.split(",") for item in line.split(" -> ")]] for line in lines]

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = 0
max_y = -sys.maxsize

for rock_line in rock_lines:
    for rock in rock_line:
        if rock["x"] > max_x:
            max_x = rock["x"]
        if rock["x"] < min_x:
            min_x = rock["x"]
        if rock["y"] > max_y:
            max_y = rock["y"]

x_length = max_x - min_x + 1 + 4  # Pad 1 for each side for sand fall, pad 1 more each side for infinity indicator (X)
y_length = max_y - min_y + 1 + 2  # Pad 2 since floor is 2 tiles below cave
for rock_line in rock_lines:
    for rock in rock_line:
        rock["x"] -= min_x
        rock["y"] -= min_y

cave = [["." if 0 < i < x_length - 1 else "X" for i in range(x_length)] for _ in range(y_length)]
cave[-1] = ["#" for _ in range(x_length)]

for rock_line in rock_lines:
    for i in range(len(rock_line) - 1):
        rock_a = rock_line[i]
        rock_b = rock_line[i + 1]

        x_direction = 1 if rock_a["x"] < rock_b["x"] else -1
        y_direction = 1 if rock_a["y"] < rock_b["y"] else -1
        for x in range(rock_a["x"], rock_b["x"] + x_direction, x_direction):
            for y in range(rock_a["y"], rock_b["y"] + y_direction, y_direction):
                cave[y][x + 2] = "#"  # Pad 2 for sand fall tile and infinity indicator

sand_starting_x = 500 - min_x + 2  # Pad 2 for sand fall tile and infinity indicator
cave[0][sand_starting_x] = "+"

sand_path = [{"x": sand_starting_x, "y": 0}]
sand_count = 0


def add_sand():
    global sand_path
    global sand_count
    sand = sand_path.pop()
    sand_count += 1
    cave[sand["y"]][sand["x"]] = "O"


while True:
    if len(sand_path) == 0:
        break

    current_sand = sand_path[-1]
    x = current_sand["x"]
    y = current_sand["y"]

    y += 1
    if y >= y_length:
        add_sand()
        continue

    if cave[y][x] == ".":
        sand_path.append({"x": x, "y": y})
        continue

    x -= 1
    if cave[y][x] == "X":
        cave[y][x] = "O"
        sand_count += y_length - y - 1
        continue

    if cave[y][x] == ".":
        sand_path.append({"x": x, "y": y})
        continue

    x += 2
    if cave[y][x] == "X":
        cave[y][x] = "O"
        sand_count += y_length - y - 1
        continue

    if cave[y][x] == ".":
        sand_path.append({"x": x, "y": y})
        continue

    add_sand()

for i in range(len(cave)):
    line = cave[i]
    print("".join(line) + " " + f'{i:03}')

print()
print(sand_count)
