import numpy as np
import re

if __name__ == '__main__':

    seedsA = [(4043382508, 113348245), (3817519559, 177922221), (3613573568, 7600537), (773371046, 400582097),
             (2054637767, 162982133), (2246524522, 153824596), (1662955672, 121419555), (2473628355, 846370595),
             (1830497666, 190544464), (230006436, 483872831)]
    files = ["aoc5_1", "aoc5_2", "aoc5_3", "aoc5_4", "aoc5_5", "aoc5_6", "aoc5_7"]
    count = 0
    fields = []
    seeds = set()

    for i, (start, len) in enumerate(seedsA):
        seeds.add(range(start, start + len))

    for file in files:

        with open(file) as f:
            lines = f.readlines();

        seeds_ = set()

        while seeds:
            r = seeds.pop()
            for line in lines:
                ll = line.split(" ")
                dest = int(ll[0])
                src = int(ll[1])
                off = int(ll[2])
                if r.start in range(src, src + off):
                    if r.stop in range(src, src + off):
                        seeds_.add(range(dest + r.start - src, dest + r.stop - src))
                    else:
                        seeds_.add(range(dest + r.start - src, dest + off))
                        seeds.add(range(src + off, r.stop))
                else:
                    if r.stop in range(src, src + off):
                        seeds_.add(range(dest, dest + r.stop - src))

        seeds = seeds_

    print(sorted(seeds, key=lambda r: r.start))
