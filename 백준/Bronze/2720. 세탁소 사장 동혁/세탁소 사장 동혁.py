# 세탁소 사장 동혁

# 테스트 케이스의 개수 T
t = int(input())

for _ in range(t):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money//i, end=' ')
        money %= i