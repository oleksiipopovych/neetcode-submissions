# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode()
        curr.next = head
        slow = fast = curr

        counter = 0
        while fast and fast.next:
            fast = fast.next
            counter += 1
            if counter > n:
                slow = slow.next;
        
        newNext = slow.next.next
        slow.next = newNext

        return curr.next


        