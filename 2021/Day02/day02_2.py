file = open('input.txt', 'r')
linesread = 0
depth, horiz, aim = 0, 0, 0
for line in file:
    linesread += 1
    for word in line.split():
        try:
            number = int(word)
            if where_to == 'forward':
                horiz += number
                depth += aim * number
            elif where_to == 'down':
                aim += number
            else:
                aim -= number
            if depth < 0:
                print("DEPTH REACHED PAST 0!")  # Never happened
                break
            if aim < 0:
                print("AIM REACHED PAST 0!")  # Never happened
        except ValueError:
            where_to = word

print(linesread)
print(depth, horiz)
print(depth * horiz)