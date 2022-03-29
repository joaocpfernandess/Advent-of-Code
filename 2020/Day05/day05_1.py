file = open('input.txt', 'r')
id_list = []
for line in file:
    rows = [i for i in range(128)]
    for i in range(7):
        if line[i]=='F':
            rows = rows[:int(len(rows)/2)]
        else:
            rows = rows[int(len(rows)/2):]
    cols = [i for i in range(8)]
    for j in range(7,10):
        if line[j] == 'L':
            cols = cols[:int(len(cols)/2)]
        else:
            cols = cols[int(len(cols)/2):]
    id_list += [rows[0]*8+cols[0]]
print(max(id_list))