file = open('input.txt', 'r')
linesread = 0
depth, horiz = 0, 0
for line in file:
    linesread += 1
    for word in line.split():
        try:
            number = int(word)
            if where_to == 'forward':
                horiz += number
            elif where_to == 'down':
                depth += number
            else:
                depth -= number
            if depth < 0:
                print("DEPTH REACHED PAST 0!")  # Never happened
                break
        except ValueError:
            where_to = word

print(linesread)
print(depth, horiz)
print(depth*horiz)