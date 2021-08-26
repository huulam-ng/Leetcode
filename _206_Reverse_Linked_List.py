# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        while (cur and cur.next):
            nextNode = cur.next
            cur.next = nextNode.next
            nextNode.next = head
            head = nextNode
        return head