# https://leetcode.com/problems/palindrome-number/

""" #casetest reverse a number
x = 1234
m = int(str(x)[::-1])
print(m)

"""

def palindrome(num):
    num = input()
    reverse_num = int(str(num)[::-1])
   
    if reverse_num[::-1] == num:
        return True
    elif reverse_num[::-1] == num:
        return False 

print(palindrome(123))


