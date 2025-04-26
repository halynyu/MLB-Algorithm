# 컵홀더

n = int(input())
seat = input()

couple = seat.count('LL')

if couple <= 1:
    print(n)
else:
    print(n + 1 - couple)