class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            vitri = 0 
            for i in nums:
                if (i < target):
                    vitri += 1
            return vitri
        