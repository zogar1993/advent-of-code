with open('2022_02.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

#A 1 Rock
#B 2 Paper
#C 3 Scissors

#X Lose
#Y Draw
#Z Win

dictionary = {
    "X": {
        "A": 3,
        "B": 1,
        "C": 2,
    },
    "Y": {
        "A": 4,
        "B": 5,
        "C": 6,
    },
    "Z": {
        "A": 8,
        "B": 9,
        "C": 7,
    }
}

score = 0
for line in lines:
    his_move = line[0]
    match_result = line[2]
    score += int(dictionary[match_result][his_move])

print(score)