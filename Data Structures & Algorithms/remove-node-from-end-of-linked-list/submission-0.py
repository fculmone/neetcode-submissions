# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        list_len = 0
        while curr:
            list_len += 1
            curr = curr.next
        pos_to_remove = list_len - n
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        for i in range(pos_to_remove):
            prev = curr
            curr = curr.next 
        # print(prev.val)
        # print(curr.val)
        prev.next = curr.next
        return dummy.next
