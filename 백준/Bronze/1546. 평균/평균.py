n = int(input())

score = list(map(int, input().split()))

max_score = max(score)
sum_score = sum(score)
avg_score = (sum_score / max_score * 100) / n

print(avg_score)