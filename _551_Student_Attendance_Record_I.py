class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        check_L = True
        for i in range(0,len(s)):
            if s[i] == 'A': 
                count_A += 1
            if "LLL" in s:
                check_L = False

        if count_A < 2 and check_L == True: return True
        else: return False