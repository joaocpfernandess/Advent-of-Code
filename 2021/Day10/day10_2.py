file = open('input.txt', 'r')

chars_dict = {'(': 0, '[': 1, '{': 2, '<': 3}
pairs_dict = {')': '(', ']': '[', '}': '{', '>': '<'}
error_list = []

for line in file:
    incompleteQ = True
    #        () [] {} <>
    layers = [0, 0, 0, 0]
    level = []
    for char in line[:-1]:
        if char in pairs_dict:
            pair = pairs_dict[char]
            ind = chars_dict[pair]
            if level[-1] == pair:
                level = level[:-1]
                layers[ind] -= 1
            else:
                incompleteQ = False
                break
        else:
            level.append(char)
            layers[chars_dict[char]] += 1

    if incompleteQ:
        level.reverse()
        err = 0
        for c in level:
            err = 5 * err + chars_dict[c] + 1
        error_list.append(err)


error_list.sort()
m = int(0.5 * (len(error_list)-1))
print(f'FINAL ANSWER: {error_list[m]}')