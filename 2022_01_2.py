with open('2022_01.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

max = [0, 0, 0]
current = 0

def update_max():
    global max
    if max[0] < current:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = current
    elif max[1] < current:
        max[2] = max[1]
        max[1] = current
    elif max[2] < current:
        max[2] = current

for line in lines:
    if line == "":
        update_max()
        current = 0
    else:
        current += int(line)
update_max()

print(sum(max))