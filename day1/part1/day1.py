import sys
nums = []
f = open("input.txt")
for line in f:
    nums.append(list(map(int, line.split())))
vysledek = 0

for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        vysledek += 1

print(vysledek)