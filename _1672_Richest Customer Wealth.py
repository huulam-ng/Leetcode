class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        for ai in accounts:
            result.append(self.sum_of_list(ai))
        return max(result)
        
    
    def sum_of_list(self, nums):
        sum = 0
        for i in nums:
            sum += i
        return sum

