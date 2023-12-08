import numpy as np
import re

filename = "aoc3_input"


def is_found(char):
    return char == '*'


if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();

    map = {(0, 0): 1}

    number = 0
    pair = ()
    isOk = False
    maxI = len(lines) - 1
    maxJ = len(lines[0]) - 2
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            if not lines[i][j].isdigit():
                if isOk:
                    if not map.__contains__(pair):
                        map[pair] = number
                    else:
                        count += map[pair] * number
                    isOk = False
                number = 0
            if lines[i][j].isdigit():
                number *= 10
                number += int(lines[i][j])
                if i > 0 and is_found(lines[i - 1][j]):
                    isOk = True
                    pair = (i - 1, j)
                if j > 0 and is_found(lines[i][j - 1]):
                    isOk = True
                    pair = (i, j - 1)
                if i > 0 and j > 0 and is_found(lines[i - 1][j - 1]):
                    isOk = True
                    pair = (i - 1, j - 1)
                if i < maxI and is_found(lines[i + 1][j]):
                    isOk = True
                    pair = (i + 1, j)
                if j < maxJ and is_found(lines[i][j + 1]):
                    isOk = True
                    pair = (i, j + 1)
                if i < maxI and j < maxJ and is_found(lines[i + 1][j + 1]):
                    isOk = True
                    pair = (i + 1, j + 1)
                if i > 0 and j < maxJ and is_found(lines[i - 1][j + 1]):
                    isOk = True
                    pair = (i - 1, j + 1)
                if i < maxI and j > 0 and is_found(lines[i + 1][j - 1]):
                    isOk = True
                    pair = (i + 1, j - 1)

    print(count)
