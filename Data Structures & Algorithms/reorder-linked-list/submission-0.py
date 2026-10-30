# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        retval = head
        def print_list(head):
            curr = head
            while curr:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")
        list_len = 0
        temp = head
        while temp:
            list_len += 1
            temp = temp.next
        list1 = head
        list2 = head
        prev = None
        count = math.ceil(list_len / 2)
        for i in range(count):
            prev = list2
            list2 = list2.next
        prev.next = None
        # print_list(list1)
        # print_list(list2)
        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        list2 = reverse_list(list2)
        while list2:
            next2 = list2.next
            next1 = list1.next
            list1.next = list2
            list2.next = next1
            list1 = next1
            list2 = next2