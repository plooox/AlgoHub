def solution(phone_book):

    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True


'''
# zip
- 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
- 2개 이상의 인자를 넘겨서 병렬 처리 가능

# unzip
- zip의 반대

# startswith
- p2가 p1으로 시작되면 True 아니면 False를 반환
'''
