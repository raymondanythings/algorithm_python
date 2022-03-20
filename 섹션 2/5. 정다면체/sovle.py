import sys

for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n, m = map(int, input().split())
        li = [0 for i in range(n + m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                li[i + j] += 1
        mx = max(li)
        for i, x in enumerate(li):
            if x == mx:
                print(i, end=" ")
        print()
