class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(0,len(s)):
            if s[i] == '#' :
                if len(stack1) != 0:    
                    stack1.pop()
            else:
                stack1.append(s[i])

        for j in range(0,len(t)):
            if t[j] == '#' :
                if len(stack2) != 0:
                    stack2.pop()
            else:
                stack2.append(t[j])

        if stack1 == stack2: return True
        else: return False