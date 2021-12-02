work = []
f = open("input.txt")
for line in f:
    cell = list(map(str, line.strip().split()))
    direction = cell[0]
    length = cell[1]
    work.append([direction, length])

updown = 0
forward = 0
aim = 0

for i in range(len(work)):
        if work[i][0] == "down":
            aim += int(work[i][1])
        elif work[i][0] == "up":
            aim -= int(work[i][1])
        else:
            forward += int(work[i][1])
            updown += ((int(work[i][1])) * aim)

print(forward*updown)

