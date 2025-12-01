"""PART 1"""
with open("day1.txt", "r") as f:
    lst = [line.strip() for line in f]

position = 50
hit_zero = 0
for instr in lst:
    direction, amount = instr[0], int(instr[1:])
    position = (
        position - amount) % 100 if direction == "L" else (position + amount) % 100
    hit_zero += position == 0
print(hit_zero)


"""PART 2"""
position = 50
hit_zero = 0
for instr in lst:
    direction, amount = instr[0], int(instr[1:])
    if direction == "L":
        hit_zero += (position-(amount % 100) <=
                     0 and position != 0) + (amount // 100)
        position = (position - amount) % 100
    else:
        hit_zero += (position+(amount % 100) >= 100 and position != 0) + \
            (amount // 100)
        position = (position + amount) % 100
    # print(position, amount, hit_zero)
print(hit_zero)
