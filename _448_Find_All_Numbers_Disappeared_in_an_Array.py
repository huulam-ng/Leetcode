class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(1,len(nums)+1):
            new_list.append(i)
        return list(set(new_list) - set(nums))  