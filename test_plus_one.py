#https://leetcode.com/problems/plus-one/

def plusone(digits):
        num_plus = digits[-1] + 1
        digits.remove(digits[-1])
        ketqua = digits.append(num_plus)
        return ketqua
        
print(plusone([1,2,3,4]))

""" casetest1
a = [1,2,3,4,5]
for i in a:
    b = (a[-1] + 1)
    print(b)
    exit()
"""

"""casetest2
a = [1,2,3,4]
b = 3
a.append(b)
print(a)
"""
