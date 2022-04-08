from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge()
def solve():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    total = 0
    Q = deque()
    ch[n // 2][n // 2] = 1
    total = li[n // 2][n // 2]
    Q.append((n // 2, n // 2))
    L = 0
    while True:
        if L == n // 2:
            break
        else:
            size = len(Q)
            for _ in range(size):
                tmp = Q.popleft()
                for j in range(4):
                    x = tmp[0] + dx[j]
                    y = tmp[1] + dy[j]
                    # print((x, y))
                    if not ch[x][y]:
                        total += li[x][y]
                        ch[x][y] = 1
                        Q.append((x, y))
        L += 1
    print(total)
    return total


solve()
