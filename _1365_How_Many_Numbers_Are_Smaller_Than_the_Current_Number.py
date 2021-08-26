class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        count = 0
        for current_index in range(len(nums)):
            for i in range(0, len(nums)):
                if nums[current_index] > nums[i]:
                    count+= 1
            result.append(count)
            count=0
        return result
