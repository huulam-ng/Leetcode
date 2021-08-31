class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = ''
        a = []
        for i in range(0, len(num)):
            result += str(num[i])
        last_result = int(result) + int(k)
        return list(str(last_result))