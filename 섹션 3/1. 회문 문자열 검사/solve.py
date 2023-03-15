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
    answer = ''
    for i in range(1, n + 1):
        s = input()
        for j in range(len(s) // 2):
            if s[j].lower() != s[(len(s)-1) - j].lower():
                answer += f'#{i} NO'
                break
        else:
            answer += f'#{i} YES'
    # answer = 0

    return answer


solve()
