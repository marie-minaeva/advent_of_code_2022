# 1
from string import ascii_lowercase, ascii_uppercase

prior_tab = {}
for i, let in enumerate(ascii_lowercase + ascii_uppercase):
    prior_tab[let] = i + 1

with open("input_3.txt", "r") as f:
    sum_prior = 0
    for line in f.readlines():
        line = line[:-1]
        ruck_1 = list(line[:int(len(line) / 2)])
        ruck_2 = list(line[int(len(line) / 2):])
        miss_item = set(ruck_1).intersection(set(ruck_2))
        sum_prior += prior_tab[list(miss_item)[0]]
print(sum_prior)



# 2
with open("input_3.txt", "r") as f:
    lines = f.readlines()

sum_prior = 0
for i in range(int(len(lines) / 3)):
    comm_items = set(list(lines[i*3][:-1])).intersection(set(list(lines[i*3 + 1][:-1])))
    badge_letter = list(comm_items.intersection(set(list(lines[i*3 + 2][:-1]))))
    sum_prior += prior_tab[badge_letter[0]]
print(sum_prior)
