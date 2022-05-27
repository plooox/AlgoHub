import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1:

        p1 = heapq.heappop(scoville)
        p2 = heapq.heappop(scoville)

        new_p = p1 + p2 * 2
        heapq.heappush(scoville, new_p)
        answer += 1

        if scoville[0] >= K:
            break

    if scoville[0] < K:
        answer = -1

    return answer
