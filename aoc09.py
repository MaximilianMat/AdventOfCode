import numpy as np
import re

filename = "aoc9_input"


def zeroes(list):
    for l in list:
        if l != 0:
            return False
    return True


if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();

    for line in lines:
        str_l = line.split(" ")
        lists = [[]]
        for str in str_l:
            lists[0].append(int(str))

        i = 0
        while not zeroes(lists[i]):
            lists.append([])
            for j in range(len(lists[i]) - 1):
                lists[i + 1].append(lists[i][j + 1] - lists[i][j])
            i += 1

        for list in lists:
            count += list.pop()

    print(count)
