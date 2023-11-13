with open('2022_10.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

cycle = 0
x = 1
result = 0
interesting_cycle = 20

for line in lines:
    if line == "noop":
        cycle += 1
        if cycle == interesting_cycle:
            result += x * interesting_cycle
            interesting_cycle += 40
    else:
        cycle += 2
        if cycle >= interesting_cycle:
            result += x * interesting_cycle
            interesting_cycle += 40
        v = int(line.split(" ")[1])
        x += v

print(result)
