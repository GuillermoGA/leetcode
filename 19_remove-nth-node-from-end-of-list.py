from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        lst = []
        node = self
        while(node):
            lst.append(node.val)
            node = node.next

        return str(lst)


class Solution:
    """
    >>> obj = Solution()
    >>> obj.removeNthFromEnd(head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n = 2)
    [1, 2, 3, 5]
    >>> obj.removeNthFromEnd(head = ListNode(1), n = 1)
    >>> obj.removeNthFromEnd(head = ListNode(1, ListNode(2)), n = 1)
    [1]
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node != None:
            length += 1
            node = node.next

        index_to_remove = length - n

        node = head
        while node != None:
            if index_to_remove == 0: # remove head
                head = head.next
                break

            elif index_to_remove == 1:  # we are in previos to skip
                node.next = node.next.next  # skip
                break
            
            else:
                # continue in next node
                index_to_remove -= 1
                node = node.next

        return head


if __name__ == "__main__":
    import doctest
    doctest.testmod()
