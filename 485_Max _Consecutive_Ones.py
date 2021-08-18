class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        save = []
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                save.append(count)
            else:
                count = 0
        if save: return max(save)
        else: return 0