
N = int(input())
score = list(map(int, input().split()))
new_score = [0] * len(score)

max_score = max(score)

for i in range(len(score)):
    new_score[i] = score[i]*100/max_score

print(sum(new_score)/len(new_score))
