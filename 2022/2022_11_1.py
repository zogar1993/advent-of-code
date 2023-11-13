with open('2022_11.txt', 'r') as file:
    text = file.read()


def inspect_item(old, operation):
    a = old if operation[0] == "old" else int(operation[0])
    b = old if operation[2] == "old" else int(operation[2])
    if operation[1] == "+":
        return a + b
    if operation[1] == "*":
        return a * b
    raise Exception("unknown operation" + operation[1])


lines = text.split("\n")
i = 0
monkeys = []
while i < len(lines):
    # skip Money x
    i += 1

    items = [int(item.strip()) for item in lines[i].split(":")[1].split(",")]
    i += 1

    operation = lines[i].split("=")[1].strip().split(" ")
    i += 1

    condition = int(lines[i].split(" ")[-1])
    i += 1

    if_true = int(lines[i].split(" ")[-1])
    i += 1

    if_false = int(lines[i].split(" ")[-1])
    i += 2

    monkeys.append({
        "items": items,
        "operation": operation,
        "condition": condition,
        "if_true": if_true,
        "if_false": if_false,
        "inspections": 0
    })

for _ in range(20):
    for monkey in monkeys:
        operation = monkey["operation"]

        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            worry_level = inspect_item(item, operation)
            worry_level //= 3

            monkey["inspections"] += 1

            destination = monkey["if_true"] if worry_level % monkey["condition"] == 0 else monkey["if_false"]
            monkeys[destination]["items"].append(worry_level)

inspections = sorted([monkey["inspections"] for monkey in monkeys])
print(inspections[-1] * inspections[-2])


