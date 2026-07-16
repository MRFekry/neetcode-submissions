# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = {}

        while head:
            if head.next is not None and head.next in hashset:
                return True
            elif head.next is None:
                return False

            hashset[head] = head.val
            head = head.next
        
        return False