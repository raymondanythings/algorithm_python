import sys

print(sys.path)
sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    li.append([0] * n)
    li.insert(0, [0] * n)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for x in li:
        x.append(0)
        x.insert(0, 0)
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if all(li[i][j] > li[i + dx[k]][j + dy[k]] for k in range(4)):
                result += 1
    return result


solve()
