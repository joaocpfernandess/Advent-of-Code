file = open('input.txt', 'r')

ingredients = {}
allergens = {}

for line in file:
    line = line[:-1]
    line = line.split(' ')
    i = 0
    ing = line[i]
    potential = []
    while ing != '(contains':
        if ing in ingredients:
            ingredients[ing] += 1
        else:
            ingredients[ing] = 1
        potential += [ing]
        i += 1
        ing = line[i]
    i += 1
    allergic = line[i]
    add = []
    while allergic[-1] != ')':
        add += [allergic[:-1]]
        i += 1
        allergic = line[i]
    add += [allergic[:-1]]
    for a in add:
        if a in allergens:
            allergens[a] += [potential]
        else:
            allergens[a] = [potential]
    #print(line)
print(len(ingredients))
print(allergens)
print(list(allergens.keys()))

probable = {}
for allergenic in allergens:
    # probable[allergenic] = []
    ings = allergens[allergenic][0]
    for i in range(1, len(allergens[allergenic])):
        add = []
        for k in allergens[allergenic][i]:
            if k in ings:
                add += [k]
        ings = add
    probable[allergenic] = ings

print(probable)


