class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for ai in nums:
            if (ai % 2 == 0):
                even.append(ai)
            else:
                odd.append(ai)
        for bi in odd:
            even.append(bi)
        return even