with open('2022_08.txt', 'r') as file:
    text = file.read()


lines = [[int(char) for char in line] for line in text.split("\n")]


row_length = len(lines[0])
visible_trees_matrix = [[True for _ in range(row_length)] for _ in lines]

for y in range(len(lines)):
    highest = 0
    for x in range(row_length):
        if lines[y][x] >= highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False

    highest = 0
    for x in range(row_length - 1, -1, -1):
        if lines[y][x] >= highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False

for x in range(row_length):
    highest = 0
    for y in range(len(lines)):
        if lines[y][x] >= highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False

    highest = 0
    for y in range(len(lines) - 1, -1, -1):
        if lines[y][x] >= highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False

result = 0
for row in visible_trees_matrix:
    for value in row:
        if value:
            result += 1

print(result)
