def solution(s):
    conv = {"on": ("one", '1'), "tw": ("two", '2'), "th": ("three", '3'), "fo": ("four", '4'), "fi": ("five", '5'), "si": (
        "six", '6'), "se": ("seven", '7'), "ei": ("eight", '8'), "ni": ("nine", '9'), "ze": ("zero", '0')}
    answer = 0

    split_list = []
    while s != "":
        if s[0].isdigit():
            split_list.append(s[0])
            s = s.replace(s[0], "", 1)
        else:
            split_list.append(conv[s[:2]][1])
            s = s.replace(conv[s[:2]][0], "", 1)
    print(split_list)
    answer = int("".join(split_list))

    return answer
