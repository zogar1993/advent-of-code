with open('2022_05.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

def has_numbers(string):
    for char in string:
        if char.isdigit():
            return True
    return False

i = 0
stacks = []
while True:
    line = lines[i]
    if has_numbers(line):
        i += 2
        break
    else:
        stack_index = 0
        while True:
            character_index = stack_index * 4 + 1
            if character_index >= len(line):
                break
            if stack_index == len(stacks):
                stacks.append([])
            character = line[character_index]
            if character != " ":
                stacks[stack_index].insert(0, character)
            stack_index += 1
    i += 1
    
while i < len(lines):
    line = lines[i]
    parts = line.split(" from ")
    iteartions = int(parts[0][len("move "):])
    parts = parts[1].split(" to ")
    origin_index = int(parts[0]) - 1
    destination_index = int(parts[1]) - 1
    origin = stacks[origin_index]
    destination = stacks[destination_index]
    while iteartions > 0:
        destination.append(origin.pop())
        iteartions -= 1
    i += 1

result = "".join([sublist[-1] for sublist in stacks])
print(result)