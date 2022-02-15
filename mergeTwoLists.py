 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        mergedSortedLists = None 
        
        if not list1 :
            
            return  list2
        
        if not list2 :
            
            return list1 
        
        if list1.val <= list2.val :
            
            mergedSortedLists = list1 
            mergedSortedLists.next = self.mergeTwoLists(list1.next , list2)
        
        else :
            
            mergedSortedLists = list2
            mergedSortedLists.next = self.mergeTwoLists(list1 , list2.next)
        
        return mergedSortedLists 
        
        
        
