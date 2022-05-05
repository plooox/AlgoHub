import math


def digitK(n, k):
    ret = ""

    while n > 0:
        n, mod = divmod(n, k)
        ret += str(mod)
    return ret[::-1]


def isPrime(k):
    if k < 2:
        return False

    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    print(digitK(n, k))
    print(digitK(n, k).split('0'))

    for ele in digitK(n, k).split('0'):
        if len(ele) > 0:
            print(ele)
            if isPrime(int(ele)):
                answer += 1

    return answer
