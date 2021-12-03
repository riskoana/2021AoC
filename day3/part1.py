code = ""
with open("input.txt") as f:
    for line in f:
        code += (line.replace("\n", ""))

ones = [0 for x in range(12)]

for i in range(len(code)):
    if code[i] == "1":
        ones[i%12] += 1

a = 0
b = 0
for i in range(len(ones)):
    if ones[i] > 500:
        a += 2**(11-i)
    else:
        b += 2**(11-i)

print(a*b)