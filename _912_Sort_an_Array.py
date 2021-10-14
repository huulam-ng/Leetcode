class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        list_length = len(nums)

        if list_length == 1:
            return nums
        mid_point = list_length // 2

        left_partition = self.sortArray(nums[:mid_point])
        right_partition = self.sortArray(nums[mid_point:])
        return merge(left_partition, right_partition)

    def merge(left, right):
    
        output = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])

        return output
