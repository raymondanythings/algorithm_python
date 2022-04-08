from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge

# 재귀 리미트 수정
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y, h):
    global board, ch, n
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            # print(ch)
            DFS(xx, yy, h)


@judge()
def solve():
    global n, board, ch, cnt
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    # BFS 활용 풀이
    # Q = deque()
    # for h in range(100):
    #     ch = [[0] * n for _ in range(n)]
    #     cnt = 0
    #     for i in range(n):
    #         for j in range(n):
    #             if not ch[i][j] and board[i][j] > h:
    #                 Q.append((i, j))
    #                 while Q:
    #                     tmp = Q.popleft()
    #                     for m in range(4):
    #                         x = tmp[0] + dx[m]
    #                         y = tmp[1] + dy[m]
    #                         if 0 <= x < n and 0 <= y < n and board[x][y] > h and not ch[x][y]:
    #                             ch[x][y] = 1
    #                             Q.append((x, y))
    #                 cnt += 1
    #     if res < cnt:
    #         res = cnt

    # DFS 활용 풀이

    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if not ch[i][j] and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    return res


solve()
