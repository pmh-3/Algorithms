# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev
    
    
 class Solution:
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rev(head)
        
    def rev(self, node, prev = None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.rev(n, node)
      
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        stack = []
        
        while head.next:
            stack.append(head)
            head = head.next
        
        while stack:
            curr = stack.pop()
            curr.next.next = curr
            curr.next = None
        
        return head
