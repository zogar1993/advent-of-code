with open('2022_01.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

max = 0
current = 0

def update_max():
    global max
    if max < current:
        max = current

for line in lines:
    if line == "":
        update_max()
        current = 0
    else:
        current += int(line)
update_max()

print(max)