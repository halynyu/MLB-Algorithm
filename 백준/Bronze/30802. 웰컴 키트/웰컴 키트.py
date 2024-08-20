n = int(input())
t_size = list(map(int, input().split()))
t, p = map(int, input().split())

num_t = 0
for t_s in t_size:
    if t_s % t == 0:
        num_t += t_s // t
    else:
        num_t += t_s // t + 1

pen_bundle = n // p
pen = n % p

print(num_t)
print(pen_bundle, pen)