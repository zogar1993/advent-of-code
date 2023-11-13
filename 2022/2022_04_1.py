with open('2022_04.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

def is_contained_by(range, container_range):
    return container_range[0] <= range[0] and range[1] <= container_range[1]

result = 0
for line in lines:
    pair = line.split(",")
    range_a = [int(x) for x in pair[0].split("-")]
    range_b = [int(x) for x in pair[1].split("-")]
    if is_contained_by(range_a, range_b) or is_contained_by(range_b, range_a):
        result += 1

print(result)