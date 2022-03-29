file = open('input.txt', 'r')

init_pos = file.tell()
file.read()
eof = file.read()
file.seek(init_pos)

passports = []
for line in file:
    stuff = []
    while line != '\n' and line != eof:
        stuff += line.split()
        line = file.readline()
    passports += [stuff]

needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for passport in passports:
    found_attr = []
    for attr in passport:
        add = ''
        for l in attr:
            if l == ':':
                break
            else:
                add += l
        found_attr += [add]
    v = 1
    for check in needed:
        if check not in found_attr:
            v = 0
            break
    valid += v
print(valid)

