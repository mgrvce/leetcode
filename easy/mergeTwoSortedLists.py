# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function for debugging
def printLL(Ls):
    r = []
    while Ls:
        r.append(Ls.val)
        Ls = Ls.next
    print(r)

# Linked List for Testing
Ls1 = ListNode(1, ListNode(2, ListNode(4)))
Ls2 = ListNode(1, ListNode(3, ListNode(4)))

Ls3 = ListNode(None)
Ls4 = ListNode(1, ListNode(2, ListNode(4)))

def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    elif list1.val < list2.val:
        newHead = list1
        list1 = list1.next
    else:
        newHead = list2
        list2 = list2.next

    tail = newHead

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        else:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

    if not list1:
        tail.next = list2
    else:
        tail.next = list1
    
    return newHead

# Test cases
test1 = mergeTwoLists(Ls1, Ls2)
test2 = mergeTwoLists(Ls3, Ls4)

printLL(test2)