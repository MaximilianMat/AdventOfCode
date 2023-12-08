import numpy as np
import re


filename = "aoc1_input"

def convert_case(match_obj):
  if match_obj.group(1) is not None:
    return "1"
  if match_obj.group(2) is not None:
    return "2"
  if match_obj.group(3) is not None:
    return "3"
  if match_obj.group(4) is not None:
    return "4"
  if match_obj.group(5) is not None:
    return "5"
  if match_obj.group(6) is not None:
    return "6"
  if match_obj.group(7) is not None:
    return "7"
  if match_obj.group(8) is not None:
    return "8"
  if match_obj.group(9) is not None:
    return "9"

if __name__ == '__main__':

    count = 0
    with open(filename) as f:
        lines = f.readlines();

    for line in lines:
        line_left = re.sub("(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)", convert_case, line, count=0, flags=0)
        line_right = re.sub("(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)", convert_case, line[::-1], count=0, flags=0)[::-1]


        match_left = re.search("\D*(?P<a>\d).*(?P<b>\d)\D*$|^\D*(?P<c>\d)\D*$", line_left)
        match_right = re.search("\D*(?P<a>\d).*(?P<b>\d)\D*$|^\D*(?P<c>\d)\D*$", line_right)
        if match_left.group("a")!= None:
            i = int(match_left.group("a")) * 10
            i += int(match_right.group("b"))
        else:
            i = int(match_left.group("c")) * 11
        count += i

    print(count)