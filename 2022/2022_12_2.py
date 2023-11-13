with open('2022_12.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

used = [[False for _ in line] for line in lines]
topography = []
paths = []
end = None

for y in range(len(lines)):
    line = lines[y]
    row = []
    for x in range(len(line)):
        character = line[x]
        if character == "S" or character == "a":
            paths.append([{"x": x, "y": y}])
            used[y][x] = True
            row.append(ord("a"))
        elif character == "E":
            end = {"x": x, "y": y}
            row.append(ord("z"))
        else:
            row.append(ord(character))
    topography.append(row)


result = None

while True:
    path = paths.pop(0)
    last = path[-1]
    x = last["x"]
    y = last["y"]

    if end["x"] == x and end["y"] == y:
        result = len(path) - 1
        break

    xx = x - 1
    if xx >= 0 and not used[y][xx] and topography[y][xx] <= topography[y][x] + 1:
        paths.append(path + [{"x": xx, "y": y}])
        used[y][xx] = True

    xx = x + 1
    if xx < len(lines[0]) and not used[y][xx] and topography[y][xx] <= topography[y][x] + 1:
        paths.append(path + [{"x": xx, "y": y}])
        used[y][xx] = True

    yy = y - 1
    if yy >= 0 and not used[yy][x] and topography[yy][x] <= topography[y][x] + 1:
        paths.append(path + [{"x": x, "y": yy}])
        used[yy][x] = True

    yy = y + 1
    if yy < len(lines) and not used[yy][x] and topography[yy][x] <= topography[y][x] + 1:
        paths.append(path + [{"x": x, "y": yy}])
        used[yy][x] = True

print(result)
