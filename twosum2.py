#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twosum2(numbers, target):
    numbers.insert(0, 0)
    for i in range (len(numbers)):
        if i == 0:
            continue
        for j in range (i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]
                
print(twosum2([-1,0], -1))