class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 0
        count = 1
        for i in range(0, len(nums)):
            if nums[current_index] != nums[i]:
                current_index += 1
                count += 1
                nums[current_index] = nums[i]
        return count