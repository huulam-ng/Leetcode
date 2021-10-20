class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        a = s.split(" ")
        for i in a[::-1]:    
            if i == '':
                continue
            else:
                result.append(i)
        return " ".join(result)