class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) & 1 == 1:
            return False

        parentheses = {'(': ')', '{': '}', '[': ']'}
        openings = ['(', '{', '[']
        stack = []

        for ch in s:

            if ch in openings:
                stack.append(ch)
            else:
                if len(stack) <= 0:
                    return False
                top = stack.pop()
                if parentheses[top] != ch:
                    return False
        if len(stack) > 0:
            return False

        return True
