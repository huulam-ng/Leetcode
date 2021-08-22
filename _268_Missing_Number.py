class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        newlist = []
        for j in range(0,nums[-1]+1):
            newlist.append(j)
        if newlist == nums: return nums[-1]+1
        for i in range(0, len(nums)):
            if nums[i] != newlist[i]:
                return i
