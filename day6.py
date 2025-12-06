"""DAY 1"""
# import math
# with open("day6.txt", "r") as f:
#     lines = [line.split() for line in f]
# res = 0
# for i in range(len(lines[0])):
#     operation = lines[-1][i]
#     if operation == "+":
#         res += sum(int(lines[j][i]) for j in range(len(lines) - 1))
#     else:
#         res += math.prod(int(lines[j][i]) for j in range(len(lines) - 1))

# print(res)


"""DAY 2"""


def solve(lines):
    grid = [list(line.rstrip('\n')) for line in lines]
    h = len(grid)
    w = max(len(row) for row in grid)

    for row in grid:
        row += [' '] * (w - len(row))

    boundaries = []
    for c in range(w):
        if all(grid[r][c] == ' ' for r in range(h)):
            boundaries.append(c)

    chunks = []
    prev = 0
    for b in boundaries + [w]:
        if b > prev:
            chunks.append((prev, b))
        prev = b + 1

    total = 0

    for (l, r) in reversed(chunks):
        bottom = ''.join(grid[-1][l:r]).strip()
        op = bottom

        numbers = []
        for c in range(l, r):
            col = [grid[r_i][c] for r_i in range(h-1)]
            digits = [x for x in col if x.isdigit()]
            if digits:
                numbers.append(int(''.join(digits)))

        if not numbers:
            continue

        if op == '+':
            val = sum(numbers)
        else:
            val = 1
            for x in numbers:
                val *= x

        total += val

    return total


with open("day6.txt") as f:
    lines = f.readlines()

print(solve(lines))
