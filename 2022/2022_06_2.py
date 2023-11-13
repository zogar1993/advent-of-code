with open('2022_06.txt', 'r') as file:
    text = file.read()

i = 0
marker_length = 14

while True:
    marker = text[i: i+marker_length]
    if len(set(marker)) == marker_length:
        break
    i += 1

print(i + marker_length)