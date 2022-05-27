from collections import defaultdict


def solution(clothes):
    answer = 1
    clothe = defaultdict(list)

    for cl in clothes:
        clothe[cl[1]].append(cl[0])
    print(clothe)

    for key, val in clothe.items():
        answer *= len(val)+1
    answer -= 1
    return answer
