# Given the head of a singly linked list head, reverse the list, and return the new head.

def reverseList(head):
    prev = None
    current = head

    while current is not None: 
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Time complexity: O(n)
# Space complexity: O(1)