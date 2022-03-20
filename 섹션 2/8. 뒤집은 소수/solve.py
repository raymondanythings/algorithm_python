import sys


def reverse(number: int) -> int:
    st = int(str(number)[::-1].lstrip("0"))
    res = 0

    # 정수형 계산법
    while number > 0:
        t = number % 10
        res = res * 10 + t
        number = number // 10
    # 1 // 10 => 0
    return st


def is_prime(number: int) -> bool:
    if number in [1, 2]:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for index in range(1, 6):
    with open(f"in{index}.txt", "rt", encoding="utf8") as sys.stdin:
        n = int(input())
        arr = list(map(int, input().split()))
        for x in arr:
            tmp = reverse(x)
            if is_prime(tmp):
                pass
                # print(tmp, end=" ")
        # print()
