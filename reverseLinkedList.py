# Given the head of a singly linked list head, reverse the list, and return the new head.


# Here's the definition of a ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    current = head

    while current is not None: 
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

reverseList(ListNode.of([1]))
reverseList(ListNode.of([1, 2]))
reverseList(ListNode.of([1, 2, 3]))

# Time complexity: O(n)
# Space complexity: O(1)