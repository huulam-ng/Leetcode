class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        re = s + t
        stack = []
        lit =[]
        for i in re:
            lit.append(i)
        lit.sort()
        for i in range(0,len(lit)):
            if stack:
                if stack[len(stack)-1] == lit[i]:
                    stack.pop()
                else: stack.append(lit[i])
            else: stack.append(lit[i])
        for i in stack:
            return i