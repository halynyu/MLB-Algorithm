while True:
    a = input()

    if a == "0":
        break

    if len(a) % 2 == 0:
        mid = len(a) // 2
        a_l = a[:mid]
        a_r = a[mid:][::-1]
        if a_l == a_r:
            print('yes')
        else:
            print('no')

    else:
        mid = len(a) // 2
        a_l = a[:mid]
        a_r = a[mid+1:][::-1]

        if a_l == a_r:
            print("yes")
        else:
            print('no')