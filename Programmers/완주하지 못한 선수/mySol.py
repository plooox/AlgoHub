from collections import defaultdict


def solution(participant, completion):
    answer = ''

    runner = defaultdict(int)
    for member in participant:
        runner[member] += 1
    for member in completion:
        runner[member] -= 1
    for key, val in runner.items():
        if val > 0:
            answer = key
            break
    return answer
