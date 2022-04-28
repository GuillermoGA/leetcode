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
    >>> l1 = ListNode(2, ListNode(4, ListNode(3)))
    >>> l2 = ListNode(5, ListNode(6, ListNode(4)))
    >>> obj.addTwoNumbers(l1 = l1, l2 = l2)
    [7, 0, 8]
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        while(l1):
            num1.append(l1.val)
            l1 = l1.next

        num2 = []
        while(l2):
            num2.append(l2.val)
            l2 = l2.next

        num1 = int("".join(list(map(lambda x: str(x), num1[::-1]))))
        num2 = int("".join(list(map(lambda x: str(x), num2[::-1]))))

        sum_num = num1 + num2

        sum_num = str(sum_num)[::-1]

        linked_list = None
        prev = None
        for digit in sum_num:
            digit = int(digit)
            if not prev:
                linked_list = ListNode(digit)
                prev = linked_list
            else:
                prev.next = ListNode(digit)
                prev = prev.next
                
        return linked_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
