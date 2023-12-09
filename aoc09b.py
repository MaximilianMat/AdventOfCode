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

        lists[0].reverse()

        i = 0
        while not zeroes(lists[i]):
            lists.append([])
            for j in range(len(lists[i]) - 1):
                lists[i + 1].append(lists[i][j] - lists[i][j+1])
            i += 1

        c = 0
        lists.reverse()
        for l in lists:
            c = l.pop() - c
        count += c

    print(count)
