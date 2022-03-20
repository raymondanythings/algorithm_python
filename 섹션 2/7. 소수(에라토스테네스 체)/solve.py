import sys


# 에라토스테네스 체
for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        arr = [0] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if arr[i] == 0:
                primes.append(i)
                for j in range(i, n + 1, i):
                    arr[j] = 1
        print(len(primes))
