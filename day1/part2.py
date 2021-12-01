nums = []
f = open("input.txt")
for line in f:
    nums.append(list(map(int, line.split())))
vysledek = 0

for i in range(len(nums)-3):
    a = int(nums[i][0])
    b = int(nums[i + 1][0])
    c = int(nums[i + 2][0])
    d = int(nums[i + 3][0])
    if (a+b+c) < (b+c+d):
        vysledek += 1

print(vysledek)