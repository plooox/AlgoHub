from collections import Counter

word = input().upper()
freq = Counter(word)

answer = ''
if len(freq) >= 2:
    top_2 = freq.most_common(2)

    if top_2[0][1] == top_2[1][1]:
        answer = "?"
    else:
        answer = top_2[0][0]
else:
    answer = freq.most_common(1)[0][0]
print(answer)
