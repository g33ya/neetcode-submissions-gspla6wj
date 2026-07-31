# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        f/s two pointers:
        right pointer moves 2x faster than left
        if left == right node, we'll know we have a cycle
        '''

        left, right = head, head

        if not head:
            return False

        while right.next and right.next.next:
            left = left.next
            right = right.next.next
            if left == right:
                return True
        return False