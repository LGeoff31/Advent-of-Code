"""PART 1"""

with open("day2.txt", "r") as f:
    lst = [line.split(",") for line in f][0]


def invalid(id):
    id = str(id)
    length = len(id)
    return length % 2 == 0 and id[:length//2] == id[length//2:] and id[0] != '0'


res = 0
for entry in lst:
    first_id, last_id = entry.split("-")
    for i in range(int(first_id), int(last_id) + 1):
        if invalid(i):
            res += i

# print(res)

"""PART 2"""

with open("day2.txt", "r") as f:
    lst = [line.split(",") for line in f][0]


def invalid(id):
    id = str(id)
    length = len(id)
    for i in range(1, (length+2) // 2):
        # for j in range(i, length):
        substring = id[0:i]
        if len(id) % len(substring) == 0 and substring * (len(id) // len(substring)) == id and substring[0] != '0':
            return True
    return False


res = 0
for entry in lst:
    first_id, last_id = entry.split("-")
    for i in range(int(first_id), int(last_id) + 1):
        if invalid(i):
            print(i)
            res += i


print(res)
