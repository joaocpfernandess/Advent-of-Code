file = open('input.txt', 'r')


def file_reader(file):
    allergens = {}
    ingredients = {}
    for line in file:
        ings_line = []
        first = True
        for word in line[:-2].split():
            if word[0] == '(':
                first = False
            elif first:
                ings_line.append(word)
                if word not in ingredients:
                    ingredients[word] = 1
                else:
                    ingredients[word] += 1
            else:
                if word[-1] == ',':
                    word = word[:-1]
                if word not in allergens:
                    allergens[word] = [ings_line]
                else:
                    allergens[word].append(ings_line)
    return allergens, ingredients


def common_allergens(allergens):
    new_allergens = {}
    for a in allergens:
        common = allergens[a][0]
        for row in allergens[a][1:]:
            keep = []
            for ing in row:
                if ing in common:
                    keep.append(ing)
            common = keep
        new_allergens[a] = common
    only_one = [True if len(new_allergens[a]) == 1 else False for a in new_allergens]
    checked = []
    while any(only_one):
        has_one = list(new_allergens)[only_one.index(True)]
        checked.append(has_one)
        ing_one = new_allergens[has_one][0]
        for other in new_allergens:
            if other != has_one:
                if ing_one in new_allergens[other]:
                    new_allergens[other].remove(ing_one)
        only_one = [True if len(new_allergens[a]) == 1 and a not in checked else False for a in new_allergens]
    return new_allergens


allergens, ingredients = file_reader(file)
new_aller = common_allergens(allergens)
can_contain = set([i for l in new_aller for i in new_aller[l]])
canon_ing_list = ''
for allergen in sorted(new_aller):
    canon_ing_list += new_aller[allergen][0] + ','

print(f'FINAL ANSWER: {canon_ing_list[:-1]}')
