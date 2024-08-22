# Given the head of a Linked List, return the length of the list.


# Here's the definition of a ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def listLength(head):
    count = 0
    node = head

    while node is not None:
        count += 1
        node = node.next
    return count

listLength(ListNode.of([1, 2, 3, 4, 5]))
listLength(ListNode.of([1, 2]))
listLength(ListNode.of([1, 1, 1]))


# Time complexity: O(n)
# Space complexity: O(1)