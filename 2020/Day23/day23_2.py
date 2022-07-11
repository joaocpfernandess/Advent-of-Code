start = [3, 1, 5, 6, 7, 9, 8, 2, 4]
start2 = start + [i for i in range(10, 1000001)]
#start2 = set(start2)


def crab_moves(cups, n_moves):
    l = len(cups)
    current_cup = cups[0]
    n = 0
    for j in range(n_moves):
        if (j+1) % 1000 == 0:
            print(f'MOVE {j+1}')
        removed = [cups[(n+3)%l], cups[(n+2)%l], cups[(n+1)%l]]

        if n == l-1:
            del cups[:3]
        elif n == l-2:
            del cups[-1]
            del cups[:2]
        elif n == l-3:
            del cups[-2:]
            del cups[0]
        else:
            del cups[n+1:n+4]

        goal = current_cup - 1
        while goal in removed or goal==0:
            goal = (goal-1) % (max(cups)+1)

        dest = cups.index(goal)
        cups.insert((dest+1), removed[0])
        cups.insert((dest+1), removed[1])
        cups.insert((dest+1), removed[2])

        displace = cups.index(current_cup) - n
        n = (n+1+displace) % l
        current_cup = cups[n]

    return cups

print(dir(start2))
after = crab_moves(start2, 10000000)
indexof1 = after.index(1)
res = after[indexof1+1] * after[indexof1+2]
print(f'FINAL ANSWER: {res}')

#after = crab_moves(start, 10000000)
#print(after)
#indexof1 = after.index(1)
#rearranged = after[indexof1+1:] + after[:indexof1]
#string = ''.join([str(i) for i in rearranged])
#print(f'FINAL ANSWER: {string}')