n = int(input())

koong = [1] * 69
koong[2] = 2
koong[3] = 4

for i in range(4, 69):
    koong[i] = koong[i - 1] + koong[i - 2] + koong[i - 3] + koong[i - 4]

for i in range(n):
    a = int(input())

    print(koong[a])