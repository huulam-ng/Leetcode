class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''
        for i in range(0, len(digits)):
            result += str(digits[i])
        last_result = int(result) + 1
        
        return list(''.join(str(last_result)))
            
        