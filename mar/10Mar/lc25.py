from typing import Optional
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        forward = later = head
        while (later != None):
            stack.append(later.val)
            later = later.next
            if (len(stack) == k):
                while (stack):
                    forward.val = stack.pop()
                    forward = forward.next
        return head