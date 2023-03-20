import sys
import os
from collections import deque

if os.name == 'nt':
    sys.path.insert(0, "\\".join(os.getcwd().split("\\")[:-2]))
else:
    sys.path.insert(0, "/".join(os.getcwd().split("/")[:-2]))
from judge import judge



def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


@judge()
def solve():
    n, l = map(int, input().split())
    members = list(map(int, input().split()))

    # 선택정렬

    # for i in range(n):
    #     min_idx = i
    #     for j in range(i + 1, n):
    #         if members[j] < members[min_idx]:
    #             min_idx = j
    #     members[i], members[min_idx] = members[min_idx], members[i]
    # print(members)

    # 버블정렬

    # cnt = n - 1
    # while cnt >= 0:
    #     for i in range(cnt):
    #         if members[i] > members[i + 1]:
    #             members[i + 1], members[i] = members[i], members[i + 1]
    #     cnt -= 1
    # print(members)

    # 삽입정렬

    # for i in range(1, n):
    #     for j in range(i, 0, -1):
    #         if members[j] < members[j - 1]:
    #             members[j], members[j - 1] = members[j - 1], members[j]
    #         else:
    #             break
    # print(members)

    # 퀵 정렬

    quick_sort(members, 0, n - 1)

    cnt = 0

    # 방법 1

    # while len(members) >= 1:
    #     if len(members) == 1:
    #         cnt += 1
    #         break
    #     if members[0] + members[-1] > l:
    #         members.pop()
    #     else:
    #         members.pop()
    #         members.pop(0)
    #     cnt += 1

    # 방법 2 => deque 활용시

    members = deque(members)
    while len(members) >= 1:
        if len(members) == 1:
            cnt += 1
            break
        if members[0] + members[-1] > l:
            members.pop()
        else:
            members.popleft()
            members.pop()
        cnt += 1

    return cnt


solve()
