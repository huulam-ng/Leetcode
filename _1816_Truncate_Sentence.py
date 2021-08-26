class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()
        result = []
        for i in range(0,k):
            result.append(a[i])
        return ' '.join(result)