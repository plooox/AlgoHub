def solution(numbers, target):
    answer = 0
    l = len(numbers)

    def dfs(idx, val):
        if idx == l:
            if val == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, val+numbers[idx])
            dfs(idx + 1, val-numbers[idx])

    dfs(0, 0)
    return answer
