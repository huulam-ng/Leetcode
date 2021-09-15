# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        for i in range(0, self.countNode(head)//2):
            head = head.next
        return head
        
    def countNode(self,head):
        count = 0
        temp = head
        while(temp):
            count += 1
            temp = temp.next
        return count