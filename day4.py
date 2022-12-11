# 1
with open("input_4.txt", "r") as f:
    count = 0
    for line in f.readlines():
        set1 = {i for i in range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)}
        set2 = {i for i in range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)}
        smaller = min(len(set1), len(set2))
        if len(set1.intersection(set2)) == smaller and len(set1) > 0 and len(set2) > 0:
            count += 1
print(count)


# 2
with open("input_4.txt", "r") as f:
    count = 0
    for line in f.readlines():
        set1 = {i for i in range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)}
        set2 = {i for i in range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)}
        if len(set1.intersection(set2)) > 0:
            count += 1
print(count)