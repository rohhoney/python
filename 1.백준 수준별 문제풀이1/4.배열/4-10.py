N = int(input())
scores = list(map(int,input().split()))

max = max(scores)
new_scores = []

for i in scores:
    new_scores.append(i/max*100)
sum = 0

for j in new_scores:
    sum += j
average = sum/N

print(average)