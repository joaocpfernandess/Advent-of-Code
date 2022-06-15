file = open('input.txt', 'r')


def file_reader(f):
    line = f.readline()
    coords, folds = [], []
    while line != '\n':
        line = line[:-1].split(',')
        coords.append([int(line[0]), int(line[1])])
        line = f.readline()
    line = f.readline()
    while line:
        line = line[:-1].split()[2].split('=')
        folds.append([line[0], int(line[1])])
        line = f.readline()
    return coords, folds


def folding_paper(coords, folds):
    prev_result = coords
    for fold in folds:
        if fold[0] == 'x':
            result = [dot for dot in prev_result if dot[0] < fold[1]]
            outside = [dot for dot in prev_result if dot not in result]
            for dot in outside:
                dist = abs(fold[1] - dot[0])
                mirrored = [dot[0] - 2*dist, dot[1]]
                if mirrored not in result:
                    result.append(mirrored)
        else:
            result = [dot for dot in prev_result if dot[1] < fold[1]]
            outside = [dot for dot in prev_result if dot not in result]
            for dot in outside:
                dist = abs(fold[1] - dot[1])
                mirrored = [dot[0], dot[1] - 2*dist]
                if mirrored not in result:
                    result.append(mirrored)
        prev_result = result
    return result


coords, folds = file_reader(file)
after_folds = folding_paper(coords, folds)
xmax, ymax = max([dot[0] for dot in after_folds]), max([dot[1] for dot in after_folds])
for j in range(ymax+1):
    line = ''
    for i in range(xmax+1):
        if [i, j] in after_folds:
            line += '#'
        else:
            line += ' '
    print(line)