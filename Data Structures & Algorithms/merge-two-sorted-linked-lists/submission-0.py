# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        dummy = ListNode(-1)
        curr = dummy
        while node1 or node2:
            if node1 and node2:
                if node1.val <= node2.val:
                    curr.next = node1
                    curr = curr.next
                    node1 = node1.next
                else:
                    curr.next = node2
                    curr = curr.next
                    node2 = node2.next
            elif node1:
                curr.next = node1
                curr = curr.next
                node1 = node1.next
            else:
                curr.next = node2
                curr = curr.next
                node2 = node2.next
        return dummy.next

        