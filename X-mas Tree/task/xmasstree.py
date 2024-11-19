MIN_LINES = 3
CHARACTER = "*"
FIRST_CHARACTER = "/"
LAST_CHARACTER = "\\"
TOP_CHARACTER = "^"
VERY_TOP_CHARACTER = "X"
BOTTOM_CHARACTER = "| |"
TRINKET_CHARACTER = "$"


def draw(lines, interval):
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



def main():
    lines, interval = input().split()
    interval = int(interval)
    if lines.isnumeric():
        lines = int(lines)
        if lines >= MIN_LINES:
            draw(lines, interval)
        else:
            print(f"Wrong input. Must be at least {MIN_LINES}.")
    else:
        print("Wrong input. Must be numeric value")


if __name__ == "__main__":
    main()


