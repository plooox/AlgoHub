def solution(s):
    answer = []
    
    if len(s) == 1:
        return 1
    
    for unit in range(1, len(s) // 2 + 1):
        cnt = 1
        res = ""
        subStr = s[:unit]
        
        for i in range(unit, len(s), unit):
            if s[i:i+unit] == subStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                res += str(cnt) + subStr
                subStr = s[i : i+unit]
                cnt = 1
        if cnt == 1:
            cnt = ""
        res += str(cnt) + subStr
        answer.append(len(res))
    
    return min(answer)