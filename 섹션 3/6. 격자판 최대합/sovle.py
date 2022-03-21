import sys


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        li = [list(map(int, input().split())) for _ in range(n)]

        # 방법 1

        largest = -1

        for i in range(n):
            sum1 = sum2 = 0
            for j in range(n):
                sum1 += li[i][j]
                sum2 += li[j][i]
            if sum1 > largest:
                largest = sum1
            if sum2 > largest:
                largest = sum2

        sum1 = sum2 = 0
        for i in range(n):
            sum1 += li[i][i]
            sum2 += li[i][n - i - 1]
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2
        print(largest)

        # 방법 2

        row = col = crs1 = crs2 = []
        for i in range(n):
            row.append(sum(li[i]))
            ar = 0
            for j in range(n):
                ar += li[j][i]
            col.append(ar)
        crs1 += [li[i][i]]
        crs2 += [li[i][n - i - 1]]
    result = list(map(max, [row, col, crs1, crs2]))
    print(max(result))
