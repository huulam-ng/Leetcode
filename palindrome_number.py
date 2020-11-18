# https://leetcode.com/problems/palindrome-number/

""" #casetest reverse a number
x = 1234
m = int(str(x)[::-1])
print(m)

"""

def palindrome(num: str()):
    reverse_num = str(num)[::-1] 
    if reverse_num == str(num):
        return True
    elif reverse_num != str(num):
        return False 



