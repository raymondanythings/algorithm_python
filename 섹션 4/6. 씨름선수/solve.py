import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    answer = 0
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=lambda x: -x[0])
    largest = 0
    for _, w in li:
        if w > largest:
            largest = w
            answer += 1
    return answer


solve()
