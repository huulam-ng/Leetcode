class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        average_value = 0

        for i in range(1,len(salary)-1):
            average_value += salary[i]
        return average_value / (len(salary)-2)