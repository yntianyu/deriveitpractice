# Given the head of a linked list head and an index i, delete the ith-to-last element, and return the new head of the linked list.

# Here's the definition of a ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def deleteNthToLastNode(head, i):
    count = 0
    node = head

    while node is not None:
        count += 1
        node = node.next

    if count == i:
        return head.next
    
    node = head

    for __ in range(count - 1 - i):
        node = node.next

    node.next = node.next.next

    return head

# Time complexity: O(n)
# Space complexity: O(1) due to constant