with open('2022_16.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

valves = {}
for line in lines:
    parts = line.replace("valves", "valve").split("valve")
    destinations = [x.strip() for x in parts[1].split(",")]
    valve = parts[0][6:8]
    rate = int(parts[0].split("=")[1].split(";")[0])
    valves[valve] = {"rate": rate, "destinations": destinations}

unreleasable = set()
for valve in valves.keys():
    if valves[valve]["rate"] == 0:
        unreleasable.add(valve)

maximum = 0
maximum_actions = []


def release_valve(current_valve, pressure_released, minutes, unreleasable, actions):
    minutes -= 1
    unreleasable = unreleasable | {current_valve}
    release_value = minutes * valves[current_valve]["rate"]
    pressure_released += release_value
    actions = actions + ["at " + str(minutes) + " release " + current_valve + " (" + str(minutes) + " * " + str(valves[current_valve]["rate"]) + " = " + str(release_value) + ")"]

    if minutes == 0:
        global maximum
        if maximum < pressure_released:
            maximum = pressure_released
            global maximum_actions
            maximum_actions = actions
        return

    for valve in valves[current_valve]["destinations"]:
            traverse_tunnel(valve, pressure_released, minutes, unreleasable, {current_valve}, actions)


def traverse_tunnel(current_valve, pressure_released, minutes, unreleasable, untraversable, actions):
    minutes -= 1
    untraversable = untraversable | {current_valve}
    actions = actions + ["at " + str(minutes) + " traverse " + current_valve]

    if minutes == 0:
        global maximum
        if maximum < pressure_released:
            maximum = pressure_released
            global maximum_actions
            maximum_actions = actions
        return

    if current_valve not in unreleasable:
        release_valve(current_valve, pressure_released, minutes, unreleasable, actions)

    for valve in valves[current_valve]["destinations"]:
        if valve not in untraversable:
            traverse_tunnel(valve, pressure_released, minutes, unreleasable, untraversable, actions)


for valve in valves["AA"]["destinations"]:
    traverse_tunnel(valve, 0, 30, unreleasable, {"AA"}, [])

for i in range(len(maximum_actions)):
    action = maximum_actions[i]
    print(str(i).zfill(2),  action)
print()
print(maximum)
