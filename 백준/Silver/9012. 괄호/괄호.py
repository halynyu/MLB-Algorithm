n = int(input())

for _ in range(n):
    par_s = input()

    stack_list = []
    answer = "YES"
    for ps in par_s:
        if ps == "(":
            stack_list.append(ps)
        else:
            if stack_list:
                stack_list.pop()
            else:
                answer = "NO"
    if stack_list:
        answer = "NO"
    print(answer)