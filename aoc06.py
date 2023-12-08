import numpy as np
import re

filename = "aoc2_input"

if __name__ == '__main__':
    count = 0

    time = 46857582
    distance = 208141212571410
    possibilities = 0

    for loading_t in range(1, time + 1):
        dist = loading_t * (time - loading_t)
        if dist > distance:
            possibilities += 1

    print(possibilities)
