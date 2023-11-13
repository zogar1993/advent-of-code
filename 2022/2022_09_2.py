with open('2022_09.txt', 'r') as file:
    text = file.read()


lines = [line.split(" ") for line in text.split("\n")]

knots = [{"x": 0, "y": 0} for _ in range(10)]

unique_tail_positions = {"0_0"}

for line in lines:
    for _ in range(int(line[1])):
        head = knots[0]
        if line[0] == "U":
            head["y"] += 1
        elif line[0] == "R":
            head["x"] += 1
        elif line[0] == "D":
            head["y"] -= 1
        elif line[0] == "L":
            head["x"] -= 1

        for i in range(9):
            heading_knot = knots[i]
            trailing_knot = knots[i + 1]

            if abs(heading_knot["x"] - trailing_knot["x"]) == 2 or abs(heading_knot["y"] - trailing_knot["y"]) == 2:
                if heading_knot["x"] > trailing_knot["x"]:
                    trailing_knot["x"] += 1
                elif heading_knot["x"] < trailing_knot["x"]:
                    trailing_knot["x"] -= 1

                if heading_knot["y"] > trailing_knot["y"]:
                    trailing_knot["y"] += 1
                elif heading_knot["y"] < trailing_knot["y"]:
                    trailing_knot["y"] -= 1

        tail = knots[9]
        unique_tail_positions.add(str(tail["x"]) + "_" + str(tail["y"]))

print(len(unique_tail_positions))
