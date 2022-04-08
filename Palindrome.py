# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.node = head ; self.res = True 
        
        def check(node1):
            if not node1: return 
            
            check(node1.next)
            if self.node.val != node1.val: self.res = False 
            self.node = self.node.next 
            
        check(head)
        return self.res  
            
        
        
