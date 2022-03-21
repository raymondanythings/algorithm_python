arr = [5, 2, 3, 4, 5, 7, 9]


"""
inf => 양의 무한대
-inf => 음의 무한대
# arrMin = float("inf")
"""
arrMin = arr[0]
for x in arr[1:]:
    if x < arrMin:
        arrMin = x
print(arrMin)
