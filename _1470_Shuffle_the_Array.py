class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        i=0
        j=len(nums)//2
        while (i < len(nums)//2 and j < len(nums)): 
            result.append(nums[i])
            i+=1
            result.append(nums[j])
            j+=1
        return result