# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # only one list (merge two lists), hence it only hava one current node
        dummy = ListNode()
        curr = dummy 



        while list1 and list2:

            if list1.val <= list2.val:
                curr.next = list1 # list 1 的這個Node 移到下一個
                list1 = list1.next  # 變成List 1 目前的Node
                curr = curr.next 
            
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if list1:
            curr.next = list1 # list 1 的這個Node 移到下一個
                
        if list2:
            curr.next = list2
               

        return dummy.next


        
        