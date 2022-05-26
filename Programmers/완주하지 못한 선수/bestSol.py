import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


'''
# Collections.Counter

- Dictionary의 확장 개념
- 더하고 빼기 가능
'''
