from collections import deque
import sys
import os

sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge


@judge(1, 2)
def solve():
    MAX = 20
    ch = [0] * (MAX + 1)
    dis = [0] * (MAX + 1)
    n, m = map(int, input().split())
    ch[n] = 1
    dis[n] = 0
    dQ = deque()
    dQ.append(n)
    print(n, m)
    while dQ:
        now = dQ.popleft()
        print(ch)
        if now == m:
            break
        for next in (now - 1, now + 1, now + 5):
            if 0 < next <= MAX:
                if not ch[next]:
                    dQ.append(next)
                    ch[next] = 1
                    dis[next] = dis[now] + 1
    return dis[m]


solve()
