


class Solution:
    
    def dem_so_chu_so(self, number):
        dem_so = 0
        while(number > 0):
            number = number // 10
            dem_so += 1
        return dem_so 

    def Find_Numbers_with_Even_Number_of_Digits(self, nums):
        count = 0
        for i in nums:
            if self.dem_so_chu_so(i) % 2 == 0:
                count += 1
        return count      

print(Solution().Find_Numbers_with_Even_Number_of_Digits([232,222,22,33,44]))  

