# 1027/1032 test cases passed
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if(x < 0):
            num = -x
            while (num>0):
                reminder = num % 10
                result = (result * 10) + reminder
                num = num // 10
            return -result
        else:
            while (x>0):
                reminder = x % 10
                result = (result * 10) + reminder
                x = x // 10
            return result
