n = int(input())
word_list = []
for _ in range(n):
    word = input()
    word_list.append(word)

word_list = list(set(word_list))
word_list.sort(key=lambda x:(len(x), x))
print(*word_list, sep="\n")