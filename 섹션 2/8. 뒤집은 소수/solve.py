import sys

sys.path.append("C:/Users/user/Documents/algorithm_python")
from judge import judge

'''
457
1. t = 7, re = 7,    x = 45
2. t = 5, re = 75,   x = 4
3. t = 4, re = 754 , x = 0
'''

def reverse(x:int):
    re = 0
    while x > 0:
        t = x % 10
        re = re * 10 + t
        x = x // 10
    # int(str(x)[::-1].lstrip('0'))
    return re

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

@judge()
def solve():
    answer = []
    n = int(input())
    nums = list(map(int,input().split()))
    for num in nums:
        t = reverse(num)
        # print(t)
        if isPrime(t):
            answer.append(t)
    return ' '.join(map(str,answer))


solve()