n = 3
target = "abcd"
p = ["P x", "L", "P y"]
result = ""
pointer = len(target)
for i in range(n):
    m = p[i].strip().split()
    v = m[0]
    if v == "P":
        target = target[:pointer] + m[1] + target[pointer:]
        pointer += 1
    elif v == "L":
        if pointer != 0:
            pointer -= 1
    elif v == "D":
        if pointer != len(target):
            pointer += 1
    elif v == "B":
        if pointer != 0:
            target = target[: pointer - 1] + target[pointer:]
            pointer -= 1

print(target)

"""
xabc

"""
