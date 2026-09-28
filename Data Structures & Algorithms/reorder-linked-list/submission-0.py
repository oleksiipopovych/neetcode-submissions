# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next
            fast = fast.next


        curr = slow.next
        slow.next = None
        prev = None;
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        res = head
        second = prev
        while second:
            first_next = res.next
            second_next = second.next
            res.next = second
            second.next = first_next
            res = first_next
            second = second_next

        
        


        

        