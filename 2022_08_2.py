with open('2022_08.txt', 'r') as file:
    text = file.read()


lines = [[int(char) for char in line] for line in text.split("\n")]


length = len(lines)
result = 0

for y in range(1, length - 1):
    for x in range(1, length - 1):
        score = 1

        for xx in range(x - 1, -1, -1):
            if lines[y][xx] >= lines[y][x] or xx == 0:
                score *= x - xx
                break

        for xx in range(x + 1, length):
            if lines[y][xx] >= lines[y][x] or xx == length - 1:
                score *= xx - x
                break

        for yy in range(y - 1, -1, -1):
            if lines[yy][x] >= lines[y][x] or yy == 0:
                score *= y - yy
                break

        for yy in range(y + 1, length):
            if lines[yy][x] >= lines[y][x] or yy == length - 1:
                score *= yy - y
                break

        if score > result:
            result = score

print(result)
