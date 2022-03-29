# Create Bag class; each bag is uniquely identified by color
class Bag:

    def __init__(self, color):
        self.color = color
        self.ia = []
        self.ic = []
        self.oc = []

    def add_inner_bag(self, color, amount):
        self.ic += [color]
        self.ia += [amount]

    def add_outer_bag(self, color):
        self.oc += [color]


def line_reader(line):
    line = line.split()
    color = line[0]+' '+line[1]
    line = line[4:]
    inner_colors, inner_amounts = None, None
    if line[0]!='no':
        line = ' '.join(line).split(',')
        inner_colors, inner_amounts = [], []
        for newbag in line:
            newbag = newbag.split()
            inner_colors += [newbag[1]+' '+newbag[2]]
            inner_amounts += [int(newbag[0])]
    return color, inner_colors, inner_amounts


file = open('input.txt', 'r')
bags = []
colors = []
for line in file:
    col, in_col, in_am = line_reader(line)
    if col not in colors:
        colors += [col]
        b = Bag(col)
        bags += [b]
    else:
        b = list(filter(lambda x: x.color == col, bags))[0]
    if in_col:
        for i in range(len(in_col)):
            if in_col[i] not in colors:
                colors += [in_col[i]]
                c = Bag(in_col[i])
                c.add_outer_bag(col)
                bags += [c]
            else:
                getbag = list(filter(lambda x: x.color == in_col[i], bags))[0]
                getbag.add_outer_bag(col)
            b.add_inner_bag(in_col[i], in_am[i])

shiny_gold_bag = list(filter(lambda x: x.color == 'shiny gold', bags))[0]


def bags_contained(color):
    bag = list(filter(lambda x: x.color == color, bags))[0]
    if bag.ic == []:
        return 0
    else:
        return sum([bag.ia[i] for i in range(len(bag.ic))]) + sum([bag.ia[c]*bags_contained(bag.ic[c]) for c in range(len(bag.ic))])


print(bags_contained('shiny gold'))

