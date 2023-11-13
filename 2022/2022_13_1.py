import json

with open('2022_13.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")


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


result = 0
for i in range((len(lines) + 1) // 3):
    line_index = i * 3
    left = json.loads(lines[line_index])
    right = json.loads(lines[line_index+1])
    value = compare_packages(left, right)
    if value:
        result += i + 1
print(result)

