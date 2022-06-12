file = open('input.txt', 'r')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# Function to associate in each digit the signal with the actual digit
def associate(line):
    # Step 0: Initialize useful stuff
    result = [None for _ in range(7)]
    used = []

    # Step 1: Count n times each letter appears on the input line
    count = [0 for _ in range(7)]
    for word in line:
        for letter in word:
            count[letters.index(letter)] += 1

    # Step 2: Associate the unique n's to their digit ('b', 'e', 'f')
    b_digit = letters[count.index(6)]  # b
    result[1] = b_digit
    used.append(b_digit)
    e_digit = letters[count.index(4)]  # e
    result[4] = e_digit
    used.append(e_digit)
    f_digit = letters[count.index(9)]  # f
    result[5] = f_digit
    used.append(f_digit)

    # Step 3: Find 1 (only 2 digits)
    one_word = [word for word in line if len(word) == 2][0]

    # Step 4: Digit in 1 that shows 9 times is 'f', other is 'c'
    for digit in one_word:
        if count[letters.index(digit)] != 9:
            result[2] = digit
            c_digit = digit
            used.append(c_digit)

    # Step 5: Get 'a' (digit that shows 8 that isn't c)
    a_digit = [l for l in letters if count[letters.index(l)] == 8 and l != c_digit][0]
    result[0] = a_digit
    used.append(a_digit)

    # Step 6: Find 4 (4 active digits)
    four_word = [word for word in line if len(word) == 4][0]

    # Step 7: Out of the remaining digits to identify, one that is in 4 is 'd', other is 'g'
    unused = [l for l in letters if l not in used]
    for u in unused:
        if u in four_word:
            d_digit = u
            result[3] = d_digit
        else:
            g_digit = u
            result[6] = g_digit

    return result


connects = [
    # a  b  c  d  e  f  g
    [1, 1, 1, 0, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 0, 1, 1, 1, 0, 1],  # 2
    [1, 0, 1, 1, 0, 1, 1],  # 3
    [0, 1, 1, 1, 0, 1, 0],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 0, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]  # 9
]


# Function to 'translate' the signals of the output numbers
def get_numbers(line):
    line = line.split(' | ')
    in_line = line[0].split()
    out_line = line[1].split()
    config = associate(in_line)
    result = ''

    for num in out_line:
        translated = []
        for l in num:
            translated.append(letters[config.index(l)])
        scheme = [1 if i in translated else 0 for i in letters]
        result += str(connects.index(scheme))

    return int(result)


print(f'FINAL RESULT: {sum([get_numbers(line) for line in file])}')
