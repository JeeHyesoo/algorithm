# define ListNode class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0) # pseudo-head
        
    def get(self, index):
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
            
        curr = self.head
        
        # index steps needed to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
        
    # add node at head
    def addAtHead(self, val):
        self.addAtIndex(0, val)
        
    # add node at tail
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
        
    # add node at index
    def addAtIndex(self, index, val):
        # if index is greater than the length, the node will not be inserted
        if index > self.size:
            return
            
        # if index is negative, the node will be inserted at the head of the list
        if index < 0:
            index = 0
            
        self.size += 1
        
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        
    # delete node at index
    def deleteAtIndex(self, index):
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
            
        self.size -= 1
        
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next
        pred.next = pred.next.next


def addTwoNumbers(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next
