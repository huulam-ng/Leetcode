# https://leetcode.com/problems/two-sum/


def twosum(nums, target):
   for i in range (len(nums)):
      for j in range(i + 1, len(nums)):
         if nums[i] + nums[j] == target:
            return [i, j]



# test git
