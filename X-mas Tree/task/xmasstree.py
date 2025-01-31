MIN_LINES = 3
CHARACTER = "*"
FIRST_CHARACTER = "/"
LAST_CHARACTER = "\\"
TOP_CHARACTER = "^"
VERY_TOP_CHARACTER = "X"
BOTTOM_CHARACTER = "| |"
TRINKET_CHARACTER = "O"
COLS = 50
ROWS = 30
SIGNATURE = "Merry Xmas"
# MATH
sig_start = (COLS - len(SIGNATURE)) // 2
arr = [[" " for i in range(COLS)] for j in range(ROWS)]


def draw_single(lines, interval):
    print(" " * (lines - 1), VERY_TOP_CHARACTER, sep='')

    counter = 0
    for line in range(1, lines + 1):
        blanks_each_side = lines - line
        signs_for_line = 2 * line - 1

        if line == 1:
            print(" " * blanks_each_side, TOP_CHARACTER * signs_for_line, sep='')
        else:
            print(" " * blanks_each_side, FIRST_CHARACTER, sep='', end='')
            for i in range(0, (signs_for_line - 2)):
                if i % 2 == 1:
                    if counter % interval == 0:
                        print(TRINKET_CHARACTER, sep='', end='')
                        counter = counter + 1
                    else:
                        print(CHARACTER, sep='', end='')
                        counter = counter + 1
                else:
                    print(CHARACTER, sep='', end='')
                    # counter = counter + 1
            print(LAST_CHARACTER, sep='')

    print(" " * (lines - 2), BOTTOM_CHARACTER, sep='')


def draw_tree(lines, interval, start_row, start_col):
    start_r = start_row  # + 1
    start_c = start_col  # + lines
    arr[start_r][start_c] = VERY_TOP_CHARACTER
    counter = 0
    for line in range(2, lines + 2):
        blanks_each_side = start_c - line + 2
        signs_for_line = 2 * line - 1
        line_r = line + start_r - 1

        if line == 2:
            arr[line_r][blanks_each_side] = TOP_CHARACTER
        else:
            arr[line_r][blanks_each_side] = FIRST_CHARACTER
            for i in range(0, (signs_for_line - 4)):
                if (i + 1) % 2 != 0:
                    arr[line_r][blanks_each_side + 1 + i] = CHARACTER
                else:
                    if counter % interval == 0 or counter == 0:
                        arr[line_r][blanks_each_side + 1 + i] = TRINKET_CHARACTER
                        counter = counter + 1
                    else:
                        arr[line_r][blanks_each_side + 1 + i] = CHARACTER
                        counter = counter + 1

            arr[line_r][blanks_each_side + signs_for_line - 3] = LAST_CHARACTER

    # arr[start_r + lines + 2][(start_c - 1):(start_c)] = BOTTOM_CHARACTER
    i = -1
    for char in BOTTOM_CHARACTER:
        arr[start_r + lines + 1][start_c + i] = char
        i += 1


def draw_array(lines, interval, start_row, start_col):
    # trees
    draw_tree(lines, interval, start_row, start_col)


def draw_card_with_border():
    # borders
    for row_num in range(ROWS):
        for i in range(COLS):
            if i == 0 or i == COLS - 1:
                arr[row_num][i] = "|"
        if row_num == 0:
            for i in range(COLS):
                arr[0][i] = "-"
        if row_num == ROWS - 4:
            for i in range(sig_start, sig_start + len(SIGNATURE)):
                arr[ROWS - 3][i] = SIGNATURE[i - sig_start]
        if row_num == ROWS - 1:
            for i in range(COLS):
                arr[ROWS - 1][i] = "-"

    for row in arr:
        for sign in row:
            print(sign, end='')
        print()


def main():
    params = input().split()
    if param_check(params):
        if len(params) == 2:
            height, interval = params[0], params[1]
            height = int(height)
            interval = int(interval)
            if height >= MIN_LINES:
                draw_single(height, interval)
            else:
                print(f"Wrong input. Must be at least {MIN_LINES}.")
        elif len(params) % 4 == 0:
            for batch in range(len(params) // 4):
                height = int(params.pop(0))
                interval = int(params.pop(0))
                start_row = int(params.pop(0))
                start_col = int(params.pop(0))
                draw_array(height, interval, start_row, start_col)
            draw_card_with_border()


def param_check(params):
    for param in params:
        if param.isalpha():
            print("Wrong input. Must be numeric value")
            return False
    return True


if __name__ == "__main__":
    main()


