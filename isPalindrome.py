def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        first = head
        second = head 
        
        while second and second.next :
            
            first = first.next 
            second = second.next.next
            
        prev = None
        curr = first 
        
        while curr :
            next = curr.next 
            curr.next = prev 
            prev = curr
            curr = next
           
        while prev : 

            if prev.val != head.val : 
                 
                return False 

            else :

                head = head.next
                prev = prev.next
                
        return True 

                    
                
        
       
