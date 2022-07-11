start = [3, 1, 5, 6, 7, 9, 8, 2, 4]


def crab_moves(cups, n_moves):
    for n in range(n_moves):
        current_cup = cups[0]
        removed = cups[1:4]
        cups = [cups[0]] + cups[4:]
        goal = current_cup - 1
        while goal not in cups:
            goal = (goal-1) % (max(cups[1:])+1)
        dest = cups.index(goal)
        cups = cups[:dest+1] + removed + cups[dest+1:]
        cups = cups[1:] + [cups[0]]
    return cups


after100 = crab_moves(start, 100)
indexof1 = after100.index(1)
rearranged = after100[indexof1+1:] + after100[:indexof1]
string = ''.join([str(i) for i in rearranged])

print(f'FINAL ANSWER: {string}')