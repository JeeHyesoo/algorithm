def reverseList1(head):
    def reverse(node, prev = None):
        if not node:
            return prev
        next, node.next, prev
        return reverse(next, node)

    return reverse(head)

def reverseList2(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev