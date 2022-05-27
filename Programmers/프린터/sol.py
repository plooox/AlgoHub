from collections import deque


def solution(priorities, location):
    answer = 0
    dq_prior = deque(zip(priorities, [i for i in range(len(priorities))]))
    while len(dq_prior):
        front = dq_prior.popleft()

        if dq_prior and max(dq_prior)[0] > front[0]:
            dq_prior.append(front)
        else:
            answer += 1
            if front[1] == location:
                break

    return answer
