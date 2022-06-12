import numpy as np

file = open('input.txt', 'r')
init = [int(n) for n in file.readline().split(',')]
pos = np.median(init)
fuel = [abs(n-pos) for n in init]

print(f'FINAL ANSWER: {sum(fuel)}')