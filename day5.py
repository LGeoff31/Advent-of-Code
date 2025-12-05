"""PART 1"""

# with open("day5.txt", "r") as f:
#     lst = [line.strip() for line in f]

# idx = lst.index("")
# ranges = [range for range in lst[:idx]]
# queries = [query for query in lst[idx+1:]]

# def valid(query):
#     for range in ranges:
#         start, end = range.split("-")
#         start = int(start)
#         end = int(end)
#         if start <= query <= end:
#             return True
#     return False


# res = 0

# for query in queries:
#     res += valid(int(query))
# print(res)

"""PART 2"""

with open("day5.txt", "r") as f:
    lst = [line.strip() for line in f]

idx = lst.index("")

ranges = []
for r in lst[:idx]:
    s, e = r.split("-")
    ranges.append((int(s), int(e)))

ranges.sort()
stack = [[ranges[0][0], ranges[0][1]]]
# print(ranges)
for i in range(1, len(ranges)):
    s, e = ranges[i]
    if s <= stack[-1][1]:
        # Overlap
        new_end = max(stack[-1][1], e)
        stack[-1][1] = new_end
    else:
        # no overlap
        stack.append([s, e])
        print(stack)

# print(stack)
print(sum(e-s+1 for s, e in stack))
