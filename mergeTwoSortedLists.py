# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLL(Ls):
    r = []
    while Ls:
        r.append(Ls.val)
        Ls = Ls.next
    
    print(r)

Ls1 = ListNode(1, ListNode(2, ListNode(4)))
Ls2 = ListNode(1, ListNode(3, ListNode(4)))

Ls3 = ListNode(5)
Ls4 = ListNode(1, ListNode(2, ListNode(4)))

def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
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

test1 = mergeTwoLists(Ls1, Ls2)
test2 = mergeTwoLists(Ls3, Ls4)

printLL(test1)

'''
ls1 = list(map(int, input("enter ints for list1: ").split()))
ls2 = list(map(int, input("enter ints for list2: ").split()))

def mergeTwoLists(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return max(list1, list2)

    newList = []

    for i in range(min(len(list1), len(list2))):
        if list1[i] < list2[i]:
            newList.append(list1[i])
            newList.append(list2[i])
        else:
            newList.append(list2[i])
            newList.append(list1[i])
    
    return newList

print(mergeTwoLists(ls1, ls2))
'''