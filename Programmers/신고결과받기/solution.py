import collections


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    dict_id = collections.defaultdict(list)
    dict_cnt = collections.defaultdict(int)
    dict_res = collections.defaultdict(int)

    for log in report:
        user, suspect = log.split(" ")
        if suspect not in dict_id[user]:
            dict_id[user].append(suspect)
            dict_cnt[suspect] += 1

    for id, v in dict_cnt.items():
        if v >= k:
            for id_ in id_list:
                if id in dict_id[id_]:
                    dict_res[id_] += 1

    for i in range(len(answer)):
        if id_list[i] in dict_res.keys():
            answer[i] = dict_res[id_list[i]]

    return answer
