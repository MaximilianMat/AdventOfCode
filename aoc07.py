import numpy as np
import re
from functools import cmp_to_key

filename = "aoc7_input"

if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines()


    def countDis(str):
        # Create an empty dictionary to store the frequency of each character
        freq = {}

        # Iterate over each character in the string
        for char in str:
            # Increment the frequency count for the character in the dictionary
            freq[char] = freq.get(char, 0) + 1

        # Return the number of distinct characters in the string
        return freq


    order = {'A': 12, 'K': 11, 'Q': 10, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0, 'J' : -1}


    def compare(hand1, hand2):
        h1 = hand1[0]
        h2 = hand2[0]
        freq1 = countDis(h1)
        freq2 = countDis(h2)
        j1 = 0
        j2 = 0
        if freq1.__contains__('J'):
            if len(freq1) != 1:
                j1 = freq1.pop('J')
        if freq2.__contains__('J'):
            if len(freq2) != 1:
                j2 = freq2.pop('J')

        if not len(freq1) == len(freq2):
            return len(freq2) - len(freq1)

        if (len(freq1) == 2 or len(freq1) == 3) and freq1[max(freq1, key=freq1.get)] + j1 != freq2[
            max(freq2, key=freq2.get)] + j2:
            rval = (freq1[max(freq1, key=freq1.get)] + j1) - (freq2[max(freq2, key=freq2.get)] + j2)
            return rval

        for i, char in enumerate(h1):
            if char != h2[i]:
                return order[char] - order[h2[i]]


    hands = []
    for line in lines:
        ll = line.split(" ")
        hands.append((ll[0], ll[1]))

    hands = sorted(hands, key=cmp_to_key(compare))
    print(hands)

    for i, hand in enumerate(hands):
        count += (i + 1) * int(hand[1])

    print(count)
