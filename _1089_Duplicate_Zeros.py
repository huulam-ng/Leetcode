class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        current = 0
        while current < len(arr):

            if arr[current] == 0:
                arr.insert(current,0)
                arr.pop()
                current+=2
            else: current += 1
        return arr