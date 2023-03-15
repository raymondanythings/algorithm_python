import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n: str = input()
    answer = 0
    for i in n:
        if i.isdecimal():
            answer = answer * 10 + int(i)
    de = 0
    for j in range(1, int(answer ** 0.5) + 1):
        if answer % j == 0:
            de += 1

    return str(answer) + str(de * 2)


solve()
