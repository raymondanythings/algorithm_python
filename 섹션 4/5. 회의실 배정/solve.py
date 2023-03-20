import sys
import os


if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    n = int(input())
    reservations = [list(map(int, input().split())) for _ in range(n)]
    reservations.sort(key=lambda x: x[1])
    answer = 0
    end_time = 0
    for s, e in reservations:
        if end_time <= s:
            end_time = e
            answer += 1
    return answer


solve()
