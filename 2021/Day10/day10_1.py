file = open('input.txt', 'r')

chars_dict = {'(': [0, 1], ')': [0, -1],
              '[': [1, 1], ']': [1, -1],
              '{': [2, 1], '}': [2, -1],
              '<': [3, 1], '>': [3, -1]}

pairs_dict = {')': ['(', 0], ']': ['[', 1],
              '}': ['{', 2], '>': ['<', 3]}
error_vals = [3, 57, 1197, 25137]
total_error = 0

for line in file:
    #       () [] {} <>
    level = []
    for char in line[:-1]:
        if char in pairs_dict:
            p = pairs_dict[char]
            pair, ind = p[0], p[1]
            if level[-1] == pair:
                level = level[:-1]
            else:
                total_error += error_vals[ind]
                break
        else:
            level.append(char)


print(f'FINAL ANSWER: {total_error}')


