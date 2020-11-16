# https://leetcode.com/problems/two-sum/


def twosum(nums, target):
    for num1 in nums:
        for i in nums:
            if num1 + i == target:
                print(nums.index(num1))
                
                
print(twosum([2,7,11,15],9))
            




