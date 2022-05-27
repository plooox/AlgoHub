from collections import deque


def solution(progresses, speeds):
    answer = []
    dq_progress = deque(progresses)
    dq_speed = deque(speeds)

    time = 0
    while len(dq_progress) > 0:

        top_progress = dq_progress[0] + time*dq_speed[0]
        if top_progress >= 100:
            ret = 0

            while len(dq_progress) > 0 and dq_progress[0] + time * dq_speed[0] >= 100:
                ret += 1
                dq_progress.popleft()
                dq_speed.popleft()

            answer.append(ret)
        time += 1
    return answer
