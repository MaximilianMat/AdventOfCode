import numpy as np
import re


filename = "aoc4_input"


if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();


    cards = []

    for line in lines:
        match = re.search("^Card(?: )+(\d+).*", line)
        card = int(match.group(1))

        line = line[9:-1]
        sp = line.split("|")

        sp1 = sp[0].split(" ")
        sp2 = sp[1].split(" ")

        s1 = set()
        s2 = set()

        for e in sp1:
            s1.add(e)
        for e in sp2:
            s2.add(e)

        s1.remove("")
        s2.remove("")

        cards.append(len(s1&s2))

    copies = [1] * len(cards)

    for i, card in enumerate(cards):
        for j in range(card):
            copies[i + j + 1] += copies[i]

    print(sum(copies))