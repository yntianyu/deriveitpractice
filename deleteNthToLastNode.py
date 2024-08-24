# Given the head of a linked list head and an index i, delete the ith-to-last element, and return the new head of the linked list.

# Here's the definition of a ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# this code works even if you're asked to delete the head of the LL
def removeNthToLastNode2(head, i):
    dummy = ListNode()
    dummy.next = head
    
    deleteNthToLastNode(dummy, i) # the above code, solved on dummy

    return dummy.next

def deleteNthToLastNode(head, i):
    
    L = head
    R = head

    # initialize the rod to length i + 1:
    for _ in range(i + 1):
        R = R.next

    # slide the rod down to the end
    while R:
        L = L.next
        R = R.next

    # delete L.next by setting L.next to L.next.next
    L.next = L.next.next

    return head

deleteNthToLastNode(ListNode.of([1, 2, 3, 4, 5]), 2)
deleteNthToLastNode(ListNode.of([1, 2, 3, 4, 5]), 5)
deleteNthToLastNode(ListNode.of([1, 2, 3, 4, 5]), 1)


# Time complexity: O(n)
# Space complexity: O(1) 