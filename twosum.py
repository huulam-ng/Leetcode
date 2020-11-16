# https://leetcode.com/problems/two-sum/


nums = [2,55,8,7,6]
target = 9
for num1 in nums:
    for i in nums:
        if num1 + i == target:
            print(nums.index(num1))
            print(nums.index(i))
            exit()
            
            




