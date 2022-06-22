from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack, checked = [], set()
        counter = Counter(s)

        for ch in s:
            counter[ch] -= 1

            if ch in checked:
                continue

            # 뒤에 붙일 문자(사전순으로 우선인 문자)가 남아있다면, 스택&집합 비우기
            while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                checked.remove(stack.pop())

            stack.append(ch)
            checked.add(ch)

        return ''.join(stack)
