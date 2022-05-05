import math
import collections


def timeTomin(t):
    h, min = map(int, t.split(':'))
    return h * 60 + min


def solution(fees, records):
    answer = []
    time_in_log = {}
    fee_log = []
    time_log = collections.defaultdict(int)

    basic_time, basic_fee, per_time, per_fee = map(int, fees)

    for record in records:
        time, id, types = record.split()
        if types == "IN":
            time_in_log[id] = time
        else:
            start = time_in_log[id]
            minute = timeTomin(time) - timeTomin(start)
            time_log[id] += minute
            del(time_in_log[id])

    for k, v in time_in_log.items():
        minute = timeTomin("23:59") - timeTomin(v)
        time_log[k] += minute

    for id, time in time_log.items():
        if time <= basic_time:
            fee_log.append([id, basic_fee])
        else:
            # f÷ee_log[id] += basic_fee + math.ceil((time - basic_time)/per_time)*per_fee
            fee_log.append(
                [id, basic_fee + math.ceil((time - basic_time)/per_time)*per_fee])

    fee_log.sort()
    answer = [val for key, val in fee_log]
    return answer
