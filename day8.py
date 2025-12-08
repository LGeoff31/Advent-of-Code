"""PART 1"""
from collections import defaultdict
from math import sqrt, prod
import pprint
with open("day8.txt", "r") as f:
    lines = [[int(i)] + [int(n) for n in line.strip().split(",")]
             for i, line in enumerate(f)]


class UnionFind:
    def __init__(self):
        self.parent = {}

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 != p2:
            self.parent[p1] = p2

    def find(self, x):
        self.parent.setdefault(x, x)

        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


def distance(p1, p2):
    a, b, c = p1
    d, e, f = p2
    return sqrt((a-d)**2 + (b-e) ** 2 + (c-f) ** 2)


def find_closest_pair():
    min_distance = 1e9
    a, b = -1, -1
    lst = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p1, p2 = lines[i][1:], lines[j][1:]
            lst.append([distance(p1, p2), lines[i][0], lines[j][0]])

    return sorted(lst)


cnt = 0
uf = UnionFind()
idx = 0
distances = find_closest_pair()
print(distances)
while idx < len(distances) and cnt < 1000:
    _, x, y = distances[idx]
    uf.union(x, y)
    cnt += 1
    idx += 1

pprint.pprint(uf.parent)

groups = defaultdict(int)
for key in range(len(lines)):
    groups[uf.find(key)] += 1
print(groups)
lst = sorted([b for a, b in groups.items()], reverse=True)
res = 1
print(lst)
for i in range(min(3, len(lst))):
    res *= lst[i]
print(res)

"""PART 2"""
with open("day8.txt", "r") as f:
    lines = [[int(i)] + [int(n) for n in line.strip().split(",")]
             for i, line in enumerate(f)]


class UnionFind:
    def __init__(self):
        self.parent = {}

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 != p2:
            self.parent[p1] = p2

    def find(self, x):
        self.parent.setdefault(x, x)

        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def complete(self):
        roots = {self.find(i) for i in range(len(lines))}
        return len(roots) == 1


def distance(p1, p2):
    a, b, c = p1
    d, e, f = p2
    return sqrt((a-d)**2 + (b-e) ** 2 + (c-f) ** 2)


def find_closest_pair():
    min_distance = 1e9
    a, b = -1, -1
    lst = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p1, p2 = lines[i][1:], lines[j][1:]
            lst.append([distance(p1, p2), lines[i][0], lines[j][0]])
            dic[lines[i][0]] = p1
            dic[lines[j][0]] = p2

    return sorted(lst)


dic = {}
cnt = 0
uf = UnionFind()
idx = 0
distances = find_closest_pair()

while idx < len(distances):
    _, x, y = distances[idx]
    uf.union(x, y)
    cnt += 1
    idx += 1
    if uf.complete():
        print(dic[x][0] * dic[y][0])
        break
