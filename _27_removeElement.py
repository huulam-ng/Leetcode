
def del_element(nums, val):
    for i in range(0,len(nums)):
        if nums[i] == val:
            nums[i] = nums[i+1]
    nums[len(nums)-1] = 0


nums = [1,2,3,4]
val = 2
del_element(nums, val)

print("done")