class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]

            if set(s) == set(suffix):
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))
        return ''
