class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for i in range(0, len(ops)):
            if ops[i] == 'C':
                stack.pop()
            elif ops[i] == 'D':
                stack.append( stack[len(stack)-1] * 2 )
            elif ops[i] == '+':
                stack.append( stack[len(stack)-1] + stack[len(stack)-2] )
            else:
                stack.append(int(ops[i]))
        return sum(stack)