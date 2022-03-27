import sys


sys.path.insert(0, "/Users/yonghyunyeob/Documents/algorithm/inflearn/pythonalgorithm_formac")
from judge import judge


@judge()
def solve():
    global n
    global ch
    global result
    n = int(input())
    ch = [0] * (n + 1)
    result = []
    DFS(1)
    return "".join(map(lambda x: " ".join(map(str, x)), result))


def DFS(v):
    if v == n + 1:
        re = []
        for i in range(1, n + 1):
            if ch[i] == 1:
                re.append(i)
        if re:
            result.append(re)

    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


solve()
