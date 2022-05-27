from collections import deque


def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    dq = deque([[1, 0]])
    while dq:
        node, length = dq.popleft()

        if visited[node] < 0:
            visited[node] = length
            length += 1
            for edge in adj[node]:
                dq.append([edge, length])

    for length in visited:
        if length == max(visited):
            answer += 1
    return answer
