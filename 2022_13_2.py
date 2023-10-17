import json

with open('2022_13.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

divider_1 = [[2]]
divider_2 = [[6]]
packages = [divider_1, divider_2]
for i in range((len(lines) + 1) // 3):
    line_index = i * 3
    packages.append(json.loads(lines[line_index]))
    packages.append(json.loads(lines[line_index + 1]))


def compare_packages(left, right):
    if type(left) == int and type(right) == int:
        return None if left == right else left < right

    left_list = left if isinstance(left, list) else [left]
    right_list = right if isinstance(right, list) else [right]
    min_length = min(len(left_list), len(right_list))

    j = 0
    while True:
        if min_length == j:
            return None if len(left_list) == len(right_list) else len(left_list) < len(right_list)
        value = compare_packages(left_list[j], right_list[j])

        if value is not None:
            return value

        j += 1


length = len(packages)
for i in range(length):
    for j in range(i + 1, length):
        if compare_packages(packages[i],  packages[j]) == False:
            packages[i], packages[j] = packages[j], packages[i]

result = 1

for i in range(length):
    if divider_1 is packages[i]:
        result *= i + 1
        break

for i in range(length):
    if divider_2 is packages[i]:
        result *= i + 1
        break
print(packages)

print(result)
