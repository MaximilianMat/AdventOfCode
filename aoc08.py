import numpy as np
import re

filename = "aoc8_input"

if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();

    instructions = "LRRLRRLLRRRLRRLRLRRRLRRLRRRLRLLRRRLRRRLRLRRRLRRLRRLRLRLLLRRRLRRRLRRLRRLRLRRRLRRLLRRLRRLRLLRLRLRRLRLLRLRLRRRLRRLRLLRLRLLRRLRLRRLLLRLRRLRRRLLLRRLRLRRRLLRRLLLRRRLRRRLLLRRLLRLRRLRLRRLLLRLRRLLLLRRLLRRRLRRLRRLRLRLLRLRRRLLRRLLRRLRRLRRLRRLRLLRRLRRRLRLRLLLRRRLLRRRLRRLRRLLLLRRRR"

    dict = {}
    positions = []
    for line in lines:
        match = re.search("^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
        dict[match.group(1)] = (match.group(2), match.group(3))
        if match.group(1).endswith("A"):
            positions.append(match.group(1))


    for p in positions:
        index = 0
        for i in range(2):
            count = 0
            while count == 0 or not p.endswith('Z'):
                char = instructions[index]
                if char == 'L':
                    p = dict[p][0]
                else:
                    p = dict[p][1]
                count += 1
                index = (index + 1) % len(instructions)
            print(p + ": count: " + str(count))

    print(count)
