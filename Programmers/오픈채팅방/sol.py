import collections

def solution(record):
    answer = []
    user = collections.defaultdict(str)
    
    for r in record:
        a = r.split(' ')
        
        if a[0] == 'Enter' or a[0] == 'Change':
            user[a[1]] = a[2]
    
    for r in record:
        a = r.split(' ')
        
        if a[0] == 'Enter':
            answer.append(str(user[a[1]]) + "님이 들어왔습니다.")
        elif a[0] == 'Leave':
            answer.append(str(user[a[1]]) + "님이 나갔습니다.") 
    
    return answer