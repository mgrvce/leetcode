# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


Ls1 = ListNode(1, ListNode(2, ListNode(4)))
Ls2 = ListNode(1, ListNode(3, ListNode(4)))

def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1 and list2:
        return list2
    if not list2 and list1:
        return list1

    if list1.val < list2.val:
        newHead = list1
    else:
        newHead = list2

    while list1 or list2:
        if not list1:
            list1 = list2
            break
        elif not list2:
            list2 = list1
            break
        elif list1.val < list2.val:
            temp = list1.next
            list1.next = list2
            list2 = list2.next
            list1 = temp 
        else:
            temp = list2.next
            list2.next = list1
            list1 = list1.next
            list2 = temp
    
    return newHead

Ls3 = mergeTwoLists(Ls1, Ls2)

'''
while Ls3:
    print(Ls3.val)
    Ls3 = Ls3.next


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