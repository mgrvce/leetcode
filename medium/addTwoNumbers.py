# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

List1 = ListNode(2, ListNode(4, ListNode(3)))
List2 = ListNode(5, ListNode(6, ListNode(4)))

List3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
List4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

def addTwo(l1, l2):
    # code here

print(addTwo(List1, List2))
print(addTwo(List3, List4))