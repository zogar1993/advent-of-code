with open('2022_03.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")

ascii_a =  ord("a")
ascii_A =  ord("A")

result = 0
for line in lines:
    middle = len(line) // 2
    compartment_a = line[:middle]
    compartment_b = line[middle:]
    for character in compartment_a:
        if character in compartment_b:
            value = ord(character)
            priority = value - ascii_a + 1 if value >= ascii_a else value - ord("A") + 27
            result += priority
            break

print(result)