class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check_list = []
        for i in nums:
            if i not in check_list:
                check_list.append(i)
            else:
                check_list.remove(i)
        return check_list.pop()