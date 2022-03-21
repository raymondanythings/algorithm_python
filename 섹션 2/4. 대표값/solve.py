import sys

for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        arr = list(map(int, input().split()))
        avg = round(sum(arr) / n)
        min = float("inf")
        for i, x in enumerate(arr):
            tmp = abs(x - avg)
            if tmp < min:
                min = tmp
                score = x
                res = i + 1
            elif tmp == min:
                if x > score:
                    score = x
                    res = i + 1
        print(avg, res)
