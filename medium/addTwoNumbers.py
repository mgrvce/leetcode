# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# print linked list
def printLL(ll):
    new = []
    curr = ll
    while curr:
        new.append(curr.val)
        curr = curr.next
    print(new)

List1 = ListNode(2, ListNode(4, ListNode(3)))
List2 = ListNode(5, ListNode(6, ListNode(4)))

List3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
List4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

def addTwo(l1, l2):

    val = l1.val +l2.val
    carry = False
    if val > 10:
        carry = True
        val = val - 10

    head = ListNode(val)
    tail = head
    l1 = l1.next
    l2 = l2.next

    while l1 and l2:
        val = l1.val +l2.val
        if carry:
            val = val + 1
            carry = False
        elif val > 10:
            carry = True
            val = val - 10
        tail.next = ListNode(val)
        l1 = l1.next
        l2 = l2.next
    
    if l1:
        tail.next = l1.next
    elif l2:
        tail.next = l2.next
    else:
        return head


printLL(List1)
printLL(List2)
# printLL(List3)
# printLL(List4)
printLL(addTwo(List1, List2))
# printLL(addTwo(List3, List4))