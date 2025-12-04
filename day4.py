"""PART 1"""
with open("day4.txt", "r") as f:
    lst = [line.strip() for line in f]

rows, cols = len(lst), len(lst[0])


def valid(r, c):
    dr_ = [-1, 0, 1]
    dc_ = [-1, 0, 1]
    cnt = 0
    for dr in dr_:
        for dc in dc_:
            if 0 <= r+dr < rows and 0 <= c+dc < cols:
                cnt += lst[r+dr][c+dc] == "@"
    print(cnt)
    return cnt-1 < 4


res = 0
for r in range(rows):
    for c in range(cols):
        if valid(r, c) and lst[r][c] == "@":
            res += 1

print(res)


"""PART 2"""
with open("day4.txt", "r") as f:
    lst = [list(line.strip()) for line in f]

rows, cols = len(lst), len(lst[0])


def valid(r, c):
    dr_ = [-1, 0, 1]
    dc_ = [-1, 0, 1]
    cnt = 0
    for dr in dr_:
        for dc in dc_:
            if 0 <= r+dr < rows and 0 <= c+dc < cols:
                cnt += lst[r+dr][c+dc] == "@"
    return cnt-1 < 4


def algo():
    res = 0
    removed = []
    for r in range(rows):
        for c in range(cols):
            if valid(r, c) and lst[r][c] == "@":
                removed.append((r, c))
                res += 1
    for r, c in removed:
        lst[r][c] = "x"
    return res


res = 0
while True:
    cnt = algo()
    if cnt == 0:
        break
    res += cnt

print(res)
