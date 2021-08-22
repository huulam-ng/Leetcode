class Solution:

    def thirdMax(self, nums: List[int]) -> int:        
        nums = list(set(nums))
        self.selection_sort(nums)
        if len(nums) > 2: return nums[-3]
        elif len(nums) == 2: return nums[1]
        elif len(nums) == 1: return nums[0]
    def selection_sort(self,arr):
        n = len(arr)
        for i in range(0, n):
            min_index = i
            for k in range(i+1, n):
                if arr[k] < arr[min_index]:
                    min_index = k  
            if (min_index != i):
                arr[min_index], arr[i] = arr[i],arr[min_index]
