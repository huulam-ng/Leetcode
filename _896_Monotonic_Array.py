class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        check_1 = False
        check_2 = False

        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                check_1 = True
            elif nums[i] < nums[i+1]:
                check_2 = True
           

        if check_1 and check_2: return False
        else: return True