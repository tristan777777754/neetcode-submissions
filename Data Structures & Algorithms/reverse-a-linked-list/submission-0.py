# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None 
        curr = head 

        
        '''
        e.g.

        0   ->  1  ->   2  -> 3 -> 4
        prev   cur    nex_node 
        head 
        '''
        while curr:
            next_node = curr.next # 1 -> 2 
            curr.next = prev # none -> 0
            prev = curr # 0 -> 1 
            curr = next_node # 1 -> 2 
        
        return prev


        

        
            

            
            
            

