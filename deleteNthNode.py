# Given the head of a linked list head and an index i, delete the ith element, and return the new head of the linked list.

# Here's the definition of a ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def delete(head, i):
    if i == 0:
        return head.next
    
    node = head 

    for _ in range(i-1):
        node = node.next

    node.next = node.next.next
    
    return head


delete(ListNode.of([0, 1, 2]), 1)
delete(ListNode.of([5, 6, 7]), 1)
delete(ListNode.of([1, 2, 3]), 0)

# Time complexity: O(n)
# Space complexity: O(1)