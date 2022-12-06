# 1
with open("input.txt", "r") as f:
    elfs = {}
    count = 1
    elfs[1] = 0
    for line in f.readlines():
        try:
            elfs[count] += int(line[:-1])
        except:
            count += 1
            elfs[count] = 0

print(max(elfs.values()))

# 2
print(sum(sorted(elfs.values(), reverse=True)[:3]))