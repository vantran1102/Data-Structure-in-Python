#https://leetcode.com/problems/insertion-sort-list/description/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        prev = dummy
        cur = head
        while cur:
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            next_node = cur.next
            cur.next = prev.next
            prev.next = cur
        cur = cur.next
        return dummy.next