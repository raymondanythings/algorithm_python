from typing import List
import sys


def calc(values: List[int]) -> int:
    acc = 0
    result = 0
    for i in values:
        if i == 1:
            acc += 1
            result += acc
        else:
            acc = 0
    return result


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        li = list(map(int, input().split()))
        print(calc(li))
