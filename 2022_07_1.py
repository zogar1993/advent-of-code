with open('2022_07.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

tree = {
    "/": { "." : 0 },
    "." : 0
}
current = tree
path = []

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
            current["."] += int(parts[0])

result = 0

def get_size_and_add_to_result(directory):
    for dir in directory.keys():
        if dir != ".":
            directory["."] += get_size_and_add_to_result(directory[dir])
    if directory["."] <= 100000:
        global result
        result += directory["."]
    return directory["."]

get_size_and_add_to_result(tree)
print(result)