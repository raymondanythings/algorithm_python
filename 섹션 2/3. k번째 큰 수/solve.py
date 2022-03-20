import sys

for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n, k = map(int, input().split())
        li = list(map(int, input().split()))
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                for m in range(j + 1, n):
                    res.add(li[i] + li[j] + li[m])
        li = list(res)
        li.sort(reverse=True)
        print(li[k - 1])
