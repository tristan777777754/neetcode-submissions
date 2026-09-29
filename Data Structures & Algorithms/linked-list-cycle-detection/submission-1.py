# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## sliding windows always combine with set()

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 

        sett = set()

        while curr:
            curr = curr.next
            if curr in sett:
                return True
            else:
                sett.add(curr)
        return False
        
      
            

    

        