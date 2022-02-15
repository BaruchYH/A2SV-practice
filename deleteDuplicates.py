 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        if head == None :
            return 
        
        if head.next != None :
            
        
            if head.val == head.next.val :
                    temp = head.next
                    head.next = head.next.next 
                    self.deleteDuplicates(head)

            else :

                self.deleteDuplicates(head.next)
                
        return head 
                
            
        
