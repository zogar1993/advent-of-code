with open('2022_03.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

ascii_a =  ord("a")
ascii_A =  ord("A")

group = []
result = 0
for line in lines:
    group.append(line)

    if len(group) == 3:
        for character in group[0]:
            if character in group[1] and character in group [2]:
                value = ord(character)
                priority = value - ascii_a + 1 if value >= ascii_a else value - ord("A") + 27
                result += priority
                break
        group = []
    
print(result)