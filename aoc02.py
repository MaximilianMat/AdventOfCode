import numpy as np
import re


filename = "aoc2_input"


if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();

    max_red = 12
    max_green = 13
    max_blue = 14

    for line in lines:
        r = []
        g = []
        b = []
        match = re.search("^Game (\d+)", line)
        game = int(match.group(1))

        draws = line.split(";")

        for draw in draws:
            match = re.search("(?:(?:(\d+) red|(\d+) green|(\d+) blue)(?:, |;)?){1,3}", draw)
            if match.group(1) is not None:
                r.append(int(match.group(1)))
            else:
                r.append(0)
            if match.group(2) is not None:
                g.append(int(match.group(2)))
            else:
                g.append(0)
            if match.group(3) is not None:
                b.append(int(match.group(3)))
            else:
                b.append(0)

        count += max(r) * max(b) * max(g)

    print(count)