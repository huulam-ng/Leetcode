class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result1 = []
        result2 = []
        for i in s:
            result1.append(i)
        for j in t:
            result2.append(j)
        result1.sort()
        result2.sort()
        if result1 == result2:
            return True
        else: return False