#https://leetcode.com/problems/single-number/
def single_number(nums):
    dic = {}
    for i in nums :
            if i in dic :
                dic[i] = 1
            else :
                dic[i] = 2
    for i in nums :
            if dic[i] == 2 :
                return i
print(single_number([2,2,1,1,5]))