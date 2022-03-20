import sys


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        li1 = list(map(int, input().split()))
        m = int(input())
        li2 = list(map(int, input().split()))

        # 방법 1
        # re = li1 + li2
        # re.sort()

        # 방법 2

        p1 = p2 = 0
        re = []
        while p1 < n and p2 < m:
            if li1[p1] <= li2[p2]:
                re.append(li1[p1])
                p1 += 1
            else:
                re.append(li2[p2])
                p2 += 1
        if p1 < n:
            re = re + li1[p1:]
        elif p2 < m:
            re = re + li2[p2:]
        for x in re:
            print(x, end=" ")
        print()
