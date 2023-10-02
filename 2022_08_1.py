with open('2022_08.txt', 'r') as file:
    text = file.read()


lines = [[int(char) for char in line] for line in text.split("\n")]


row_length = len(lines[0])
visible_trees_matrix = [[True for _ in range(row_length)] for _ in lines]

for y in range(len(lines)):
    highest_tree = 9
    highest = -1
    for x in range(row_length):
        if lines[y][x] > highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False
            if lines[y][x] == highest_tree:
                break
    highest_tree = highest

    highest = -1
    for x in range(row_length - 1, -1, -1):
        if lines[y][x] > highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False
            if highest == highest_tree:
                break

result = 0
for x in range(row_length):
    highest_tree = 9
    highest = -1
    for y in range(len(lines)):
        if lines[y][x] > highest:
            highest = lines[y][x]
            visible_trees_matrix[y][x] = False
            if highest == highest_tree:
                break

    highest = -1
    for y in range(len(lines) - 1, -1, -1):
        if lines[y][x] > highest:
            highest = lines[y][x]
            result += 1
        elif not visible_trees_matrix[y][x]:
            result += 1

print(result)
