"""PART 1"""
# from collections import defaultdict
# with open("day3.txt", "r") as f:
#     lst = [line.strip() for line in f]


# def max_val(battery):
#     dic = defaultdict(list)
#     for i, n in enumerate(battery):
#         dic[int(n)].append(i)

#     for i in range(9, -1, -1):
#         if not dic[i]:
#             continue
#         first_idx = int(dic[i][0])
#         for j in range(9, -1, -1):
#             if not dic[j]:
#                 continue
#             last_idx = int(dic[j][-1])
#             if last_idx > first_idx:
#                 return int(str(i) + str(j))


# res = 0
# for battery in lst:
#     res += max_val(battery)
#     print(max_val(battery))

# print(res)

"""PART 2"""


def max_subsequence_12(battery):
    n = len(battery)
    k = 12
    res = []
    start = 0

    for remaining in range(k, 0, -1):
        end = n - remaining
        max_digit = '0'
        max_idx = start
        for i in range(start, end + 1):
            if battery[i] > max_digit:
                max_digit = battery[i]
                max_idx = i
        res.append(max_digit)
        start = max_idx + 1

    return int("".join(res))


with open("day3.txt", "r") as f:
    lst = [line.strip() for line in f]

res = 0
for battery in lst:
    res += max_subsequence_12(battery)
print(res)
