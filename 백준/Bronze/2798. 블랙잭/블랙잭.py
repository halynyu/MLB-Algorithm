from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

comb_list = combinations(cards, 3)

max_num = 0
for i in comb_list:
    num = sum(i)

    if num == m:
        max_num = num
        break

    else:
        if num <= m and num > max_num:
            max_num = num

print(max_num)