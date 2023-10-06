from textwrap import wrap

with open('2022_10.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

cycle = 0
x = 1
WIDTH = 40
HEIGHT = 6

result = ["." for _ in range(WIDTH * HEIGHT)]

for line in lines:
    if line == "noop":
        if x - 1 <= cycle % 40 <= x + 1:
            result[cycle] = "#"
        cycle += 1
    else:
        if x - 1 <= cycle % 40 <= x + 1:
            result[cycle] = "#"
        cycle += 1

        if x - 1 <= cycle % 40 <= x + 1:
            result[cycle] = "#"
        cycle += 1

        v = int(line.split(" ")[1])
        x += v

for line in wrap("".join(result), 40):
    print(line)
