def solution(new_id):
    answer = ''

    # step1
    step1 = new_id.lower()
    print(step1)
    # step2
    step2_li = []
    for ch in step1:
        if ch.isalnum() or ch == '-' or ch == '_' or ch == '.':
            step2_li.append(ch)
    step2 = "".join(step2_li)
    print(step2)
    # step3
    step3_li = []
    step3_li.append("#")
    for ch in step2:
        if ch == '.':
            if step3_li[-1] != '.':
                step3_li.append(ch)
        else:
            step3_li.append(ch)
    step3 = ''.join(step3_li[1:])
    print(step3)
    # step4
    step4 = step3
    if step3[0] == '.':
        step4 = step3[1:]
    if step3[-1] == '.':
        step4 = step4[:len(step4)-1]
    print(step4)
    # step5
    if len(step4) == 0:
        step5 = "a"
    else:
        step5 = step4
    print(step5)
    # step6
    if len(step5) >= 16:
        step6 = step5[:15]
        if step6[-1] == '.':
            step6 = step6[:len(step6)-1]
    else:
        step6 = step5
    print(step6)
    # step7
    if len(step6) <= 2:
        while len(step6) < 3:
            step6 += step6[-1]
    answer = step6

    return answer
