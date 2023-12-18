class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergeNode = mergeHead = ListNode(None)

        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val < node2.val:
                mergeNode.next = node1
                node1 = node1.next
            else:
                mergeNode.next = node2
                node2 = node2.next
            mergeNode = mergeNode.next
        
        while node1:
            mergeNode.next = node1
            mergeNode = mergeNode.next
            node1 = node1.next

        while node2:
            mergeNode.next = node2
            mergeNode = mergeNode.next
            node2 = node2.next

        return mergeHead.next