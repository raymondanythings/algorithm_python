import sys

for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        leng = int(input())
        for x in range(leng):
            st = input().lower()

            # 방법 1
            if st == st[::-1]:
                print(f"#{x+1} YES")
            else:
                print(f"#{x+1} NO")

            # 방법 2
            size = len(st)
            for j in range(size // 2):
                if st[j] != st[-1 - j]:
                    print(f"#{x+1} NO")
                    break
            else:
                print(f"#{x+1} YES")
