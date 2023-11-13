with open('2022_02.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

#AX 1 Rock
#BY 2 Paper
#CZ 3 Scissors

dictionary = {
    "X": {
        "C": 7,
        "A": 4,
        "B": 1,
    },
    "Y": {
        "A": 8,
        "B": 5,
        "C": 2,
    },
    "Z": {
        "B": 9,
        "C": 6,
        "A": 3,
    }
}

score = 0
for line in lines:
    his_move = line[0]
    my_move = line[2]
    score += int(dictionary[my_move][his_move])

print(score)