class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result1 = []
        result2 = []
        for i in range(0, len(word1)):
            result1 += word1[i]
        for j in range(0, len(word2)):
            result2 += word2[j]
        if result1 == result2: return True
        else: return False