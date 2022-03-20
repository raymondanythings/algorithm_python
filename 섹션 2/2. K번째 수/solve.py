import sys

for index in range(1, 6):
    result = open(f"out{index}.txt", "rt", encoding="utf8")
    sys.stdin = open(f"in{index}.txt", "rt", encoding="utf8")

    T = int(input())
    for i in range(T):
        N, s, e, k = map(int, input().split())
        arr = list(map(int, input().split()))[s - 1 : e]
        arr.sort()
        solve = f"#{i+1} {arr[k - 1]}"
        print(solve)
    print(" -- next --")
