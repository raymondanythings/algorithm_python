import sys


for index in range(1, 2):
    with open(f"in1.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        li = [list(map(int, input().split())) for _ in range(n)]
        print(li)
