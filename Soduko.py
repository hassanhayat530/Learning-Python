import sys

sudoku = []

for row in sys.stdin:
    row = row.replace('\n', '')
    row = row.split(' ')
    sudoku.append(row)


def check_rows(sudo):
    x = 0

    for row in sudo:
        nums = []
        for num in row:
            if num not in nums:
                nums.append(num)
            else:
                x += 1
                break
    return x


def check_cols(sudo):
    x = 0

    for col in range(len(sudo)):
        nums = []
        for row in sudo:
            if row[col] not in nums:
                nums.append(row[col])
            else:
                x += 1
                break
    return x


def check_blocks(sudo):
    x = 0
    num_i = 0
    for block in range(9):
        nums = []
        correct = True
        row_n = block // 3 * 3
        if block < 3:
            row_n = 0
        if block == 0 or block == 3 or block == 6:
            num_i = 0
        if block == 1 or block == 4 or block == 7:
            num_i = 3
        if block == 2 or block == 5 or block == 8:
            num_i = 6
        for row in range(row_n, row_n + 3):
            if not correct:
                break
            for num in range(num_i, num_i + 3):
                num_1 = sudo[row][num]
                if num_1 not in nums:
                    nums.append(num_1)
                else:
                    x += 1
                    correct = False
                    break
    return x

print(check_rows(sudoku) + check_cols(sudoku) + check_blocks(sudoku))
