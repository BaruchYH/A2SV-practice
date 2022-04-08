# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        node1 = head
        node2 = head.next
        node1.next = head.next.next
        node2.next = node1
        head = node2
        node2 = node1
        
        while True:
            if not node2.next: return head  
            if not node2.next.next: return head  
            node3 = node2.next
            node2.next = node2.next.next 
            node3.next = node2.next.next
            node2 = node2.next
            node2.next = node3
            node2 = node3
            
        
            
        return head 
        
        
