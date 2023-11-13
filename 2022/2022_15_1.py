with open('2022_15.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

sensor_beacon_pairs = []
for line in lines:
    parts = line.split("=")
    pair = {
        "sensor": {
            "x": int(parts[1].split(",")[0]),
            "y": int(parts[2].split(":")[0])
        },
        "beacon": {
            "x": int(parts[3].split(",")[0]),
            "y": int(parts[4])
        },
    }
    sensor_beacon_pairs.append(pair)

target_row = 2000000
non_beacon_ranges = []

for pair in sensor_beacon_pairs:
    sensor = pair["sensor"]
    beacon = pair["beacon"]
    sensor_x = sensor["x"]
    sensor_y = sensor["y"]

    distance_x = abs(sensor_x - beacon["x"])
    distance_y = abs(sensor_y - beacon["y"])
    distance = distance_x + distance_y
    distance_to_target_row = abs(sensor_y - target_row)

    if distance_to_target_row > distance:
        continue

    offset = distance - distance_to_target_row
    non_beacon_ranges.append({
        "min": sensor_x - offset,
        "max": sensor_x + offset
    })

for i in range(len(non_beacon_ranges) - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        range_i = non_beacon_ranges[i]
        range_j = non_beacon_ranges[j]
        if range_i["min"] > range_j["max"] or range_j["min"] > range_i["max"]:
            continue
        non_beacon_ranges[j] = {
            "min": min(range_i["min"], range_j["min"]),
            "max": max(range_i["max"], range_j["max"])
        }
        non_beacon_ranges.pop(i)
        break

target_row_beacon_x_positions = set()
for pair in sensor_beacon_pairs:
    beacon = pair["beacon"]
    if beacon["y"] == target_row:
        target_row_beacon_x_positions.add(beacon["x"])


result = 0
for target_row_range in non_beacon_ranges:
    result += abs(target_row_range["max"] - target_row_range["min"] + 1)
    for x in target_row_beacon_x_positions:
        if target_row_range["min"] <= x <= target_row_range["max"]:
            result -= 1

print(result)
