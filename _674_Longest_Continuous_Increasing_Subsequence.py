class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        temp = 1 
        if len(nums) == 1: return 1
        else:    
            for i in range(0,len(nums)-1):
                if nums[i+1] > nums[i]:
                    count += 1
                else: 
                    count = 1
                temp = max(count, temp)
        return temp