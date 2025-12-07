"""PART 1"""
from functools import cache
with open("day7.txt", "r") as f:
    print(type(f))
    lst = [line.strip() for line in f]
print(lst)
dp = [0] * len(lst[0])
s_index = lst[0].index("S")
dp[s_index] = 1
splits = 0
for line in lst[1:]:
    for i in range(len(line)):
        if line[i] == "^" and dp[i] == 1:
            dp[i] = 0
            splits += 1
            dp[i+1] = 1
            dp[i-1] = 1
    print(splits, dp)
print(splits)


"""PART 2"""
with open("day7.txt", "r") as f:
    print(type(f))
    lst = [line.strip() for line in f]
print(lst)


@cache
def dfs(level, idx):
    if level == len(lst):
        return 1
    res = 0
    if lst[level][idx] == "^":
        res += dfs(level + 1, idx + 1)
        res += dfs(level + 1, idx - 1)
    else:
        res += dfs(level + 1, idx)
    return res


print(dfs(1, lst[0].index("S")))
