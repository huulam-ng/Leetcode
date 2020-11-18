# https://leetcode.com/problems/two-sum/


def twosum(nums, target):
    for num1 in nums:
        for i in nums:    
            if num1 + i == target:
                return [nums.index(num1), nums.index(i)]
            




