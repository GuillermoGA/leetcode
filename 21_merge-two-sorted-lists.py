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
    >>> obj.mergeTwoLists(list1 = ListNode(1, ListNode(2, ListNode(4))), list2 = ListNode(1, ListNode(3, ListNode(4))))
    [1, 1, 2, 3, 4, 4]
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        total_length = 0
        node = list1
        while node != None:
            total_length += 1
            node = node.next
        node = list2
        while node != None:
            total_length += 1
            node = node.next

        merged_list = None
        prev_node = None
        for i in range(total_length):
            min_node = None
            if not list1:
                min_node = list2
                list2 = list2.next
            elif not list2:
                min_node = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                min_node = list1
                list1 = list1.next
            else:
                min_node = list2
                list2 = list2.next

            # Initialize
            if not merged_list:
                merged_list = min_node
                prev_node = merged_list
                continue

            prev_node.next = min_node
            prev_node = min_node

        return merged_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
