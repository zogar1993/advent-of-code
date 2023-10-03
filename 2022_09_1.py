with open('2022_09.txt', 'r') as file:
    text = file.read()


lines = [line.split(" ") for line in text.split("\n")]

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

unique_tail_positions = {"0_0"}
array = ["0_0 0_0"]

for line in lines:
    for _ in range(int(line[1])):
        if line[0] == "U":
            head_y += 1
        elif line[0] == "R":
            head_x += 1
        elif line[0] == "D":
            head_y -= 1
        elif line[0] == "L":
            head_x -= 1

        if abs(head_x - tail_x) == 2 or abs(head_y - tail_y) == 2:
            if head_x > tail_x:
                tail_x += 1
            elif head_x < tail_x:
                tail_x -= 1

            if head_y > tail_y:
                tail_y += 1
            elif head_y < tail_y:
                tail_y -= 1
        array.append(str(head_x) + "_" + str(head_y) + " " + str(tail_x) + "_" + str(tail_y))
        unique_tail_positions.add(str(tail_x) + "_" + str(tail_y))

for item in array:
    print(item)

print(len(unique_tail_positions))
