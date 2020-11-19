def searchinsertposition(nums, target: int):
        if target in nums:
            return nums.index(target)
        else:
            vitri = 0
            for i in nums:
                if i < target:
                    vitri = vitri + 1
            return vitri     
print(searchinsertposition([1,2,4,5],3))