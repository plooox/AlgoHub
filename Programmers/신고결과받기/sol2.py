
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dict_cnt = {x: 0 for x in id_list}

    for re in set(report):
        dict_cnt[re.split(" ")[1]] += 1
    print(dict_cnt)

    for re in set(report):
        if dict_cnt[re.split(" ")[1]] >= k:
            answer[id_list.index(re.split(" ")[0])] += 1

    return answer
