nums = []
f = open("input.txt")
for line in f:
    nums.append(int(line))
vysledek = 0

for i in range(len(nums)-3):
    a = int(nums[i])
    b = int(nums[i + 1])
    c = int(nums[i + 2])
    d = int(nums[i + 3])
    if (a+b+c) < (b+c+d):
        vysledek += 1

print(vysledek)