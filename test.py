"""
-10 -10 2 3 3 6 7 10 10

"""
n = 10
h_list = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
h_list.sort()
m = 8
t_list = [10, 9, -5, 2, 3, 4, 5, -10]
t_list.sort()

for i in h_list:
    lt = 0
    rt = n - 1
    cnt = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if i < t_list[mid]:
            rt = mid - 1
        else:
            cnt += 1
            lt = mid + 1

    print(cnt)
