with open('2022_07.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

tree = {
    "/": { "." : 0 },
    "." : 0
}
current = tree
path = []

occupied_space = 0

for line in  lines:
    if line.startswith("$"):
        command_cd = "$ cd "
        if line.startswith(command_cd):
            dir = line[len(command_cd):]
            if dir == "..":
                latest = path.pop()
                current = tree
                for dir in path:
                    current = current[dir]
            else:
                path.append(dir)
                current = current[dir]
    else:
        parts = line.split(" ")
        if (parts[0] == "dir"):
            current[parts[1]] = { "." : 0 }
        else:
            size = int(parts[0])
            current["."] += size
            occupied_space += size

folder_sizes = []

DISK_SPACE = 70000000
TOTAL_REQUIRED_SPACE = 30000000
required_space = TOTAL_REQUIRED_SPACE - (DISK_SPACE - occupied_space)

stack = []

def get_size_and_add_to_result(directory):
    for dir in directory.keys():
        if dir != ".":
            directory["."] += get_size_and_add_to_result(directory[dir])

    global folder_sizes
    size = directory["."]

    if (size >= required_space):
        folder_sizes.append(size)
    return directory["."]

get_size_and_add_to_result(tree)

result = min(folder_sizes)

print(result)



