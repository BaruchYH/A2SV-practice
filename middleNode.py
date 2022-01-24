 def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = head 
        last = head 
        
        while last and last.next :
            
            first = first.next 
            
            last = last.next.next 
            
        head = first 
        
        return head 
