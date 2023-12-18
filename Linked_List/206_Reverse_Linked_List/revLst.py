class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        node = head
        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev