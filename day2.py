# 1
loose_strat = {"A": "Z", "B": "X", "C": "Y"}
drawn_strat = {"A": "X", "B": "Y", "C": "Z"}
win_strat = {"A": "Y", "B": "Z", "C": "X"}
scoring = {"X": 1, "Y": 2, "Z": 3}

sum = 0
with open("input_2.txt", "r") as f:
    for line in f.readlines():
        chars = line.split(" ")
        sum += scoring[chars[1][:-1]]
        if chars[1][:-1] == drawn_strat[chars[0]]:
            sum += 3
        elif chars[1][:-1] == win_strat[chars[0]]:
            sum += 6

print(sum)


# 2
sum_2 = 0
with open("input_2.txt", "r") as f:
    for line in f.readlines():
        chars = line.split(" ")
        if chars[1][:-1] == "Y":
            sum_2 += scoring[drawn_strat[chars[0]]]
            sum_2 += 3
        elif chars[1][:-1] == "Z":
            sum_2 += scoring[win_strat[chars[0]]]
            sum_2 += 6
        else:
            sum_2 += scoring[loose_strat[chars[0]]]

print(sum_2)