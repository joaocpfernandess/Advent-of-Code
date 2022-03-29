import numpy as np


class Board:

    def __init__(self, numbers):
        self.numbers = numbers
        self.marks = np.zeros((5,5))

    # Returns True if a number was marked and False if not
    def marknumber(self, n):
        i = 0
        for line in self.numbers:
            if n in line:
                self.marks[i][line.index(n)] = 1
                return True
            i += 1
        return False

    def boardwinQ(self):
        for line in self.marks:
            if all(map(lambda x: True if x==1 else 0, line)):
                return True
        transposed = np.transpose(self.marks)
        for line2 in transposed:
            if all(map(lambda x: True if x==1 else 0, line2)):
                return True
        return False


file = open('input.txt', 'r')
nrs_list = [int(n) for n in file.readline().split(',')]

init_pos = file.tell()
file.read()
eof = file.read()
file.seek(init_pos)

boards = []
for line in file:
    nr = []
    while line != '\n' and line != eof:
        add = []
        line = line.split()
        for n in line:
            add += [int(n)]
        nr += [add]
        line = file.readline()
    if nr:
        boards += [Board(nr)]

i = 0
while i < len(nrs_list) and len(boards)!=1:
    j = 0
    while j < len(boards):
        if boards[j].marknumber(nrs_list[i]):
            if boards[j].boardwinQ():
                boards.remove(boards[j])
                j -= 1
        j += 1
    i += 1

last_board = boards[0]
while not last_board.boardwinQ():
    last_board.marknumber(nrs_list[i])
    i += 1
winning_number = nrs_list[i-1]

unmarked_last = 0
for i in range(5):
    for j in range(5):
        if last_board.marks[i][j] == 0:
            unmarked_last += last_board.numbers[i][j]

score = unmarked_last * winning_number
print(score)