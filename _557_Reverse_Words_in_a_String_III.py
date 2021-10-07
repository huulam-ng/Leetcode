class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        result = ''
        for i in a:
            result+=i[::-1]
            result+=' '
        return result[:-1]