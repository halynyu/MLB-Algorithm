while True:
    arr = list(map(int, input().split()))

    if sum(arr) == 0:
        break

    max_value = max(arr)
    arr.remove(max_value)

    s_value = 0
    for i in arr:
        s_value += i ** 2

    if s_value == max_value ** 2:
        print("right")
    else:
        print("wrong")