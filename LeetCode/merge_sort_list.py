class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge(self,list1,list2):
    dummy = ListNode(0)
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1list1 = list1.next
        else:
            cur.next = list2list2 = list2.next
        cur = cur.nex
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
    return dummy.next