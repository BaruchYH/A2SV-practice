class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for x in nums1 :
            j = 1
            if x in nums2 and x != nums2[-1] :
                while nums2[nums2.index(x)+j] < x :
                    j += 1
                    if nums2.index(x)+j == len(nums2):
                        j = j -1 
                        break
                if nums2[nums2.index(x)+j] > x :
                    stack.append(nums2[nums2.index(x)+j])
                else :
                    stack.append(-1)
            else :
                    stack.append(-1)
        return stack
                    
