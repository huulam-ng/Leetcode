#https://leetcode.com/problems/merge-two-sorted-lists/

def mergetwosortedlists(l1 = [], l2 = []):
    array = l1 + l2
    sapxep = sorted(array)
    return sapxep
print(mergetwosortedlists([1,3,2,4],[4,4,2,4]))
        
