file = open('input.txt', 'r')

timestamp = int(file.readline())
line = file.readline().split(',')
ids = [int(n) for n in line if n != 'x']
firstavailable = [i * (timestamp // i) if i * (timestamp // i) == timestamp else i * ((timestamp // i)+1) for i in ids]

correct_id = ids[firstavailable.index(min(firstavailable))]
waiting_time = min(firstavailable) - timestamp

print(correct_id * waiting_time)

