import sys

sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge
def solve():
    n = int(input())
    result = 0
    li = [list(map(int, input().split())) for _ in range(n)]

    # 방법 1
    for x in range(n):
        ab = n // 2 # 2
        num = abs(ab - x) # 2 - 1 = 1
        last = n - num # 5 - 1 = 4
        result += sum(li[x][num:last]) # 1 : 4

    # 방법 2
    # s = e = n // 2
    # for x in range(n):
    #     for y in range(s, e + 1):
    #         print(x, y)
    #         result += li[x][y]
    #     if x < n // 2:
    #         s -= 1
    #         e += 1
    #     else:
    #         s += 1
    #         e -= 1

    return result


solve()
