class LinkedListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next


def removeNthNode(nums, n):
    count = 0
    ## need to create the node method
    temp_nums = LinkedListNode(None)

    temp_nums.next = nums

    curr = temp_nums

    # here we determine the linked list length
    while(temp_nums.next is not None):
        count+= 1
        temp_nums = temp_nums.next
    print(count)


    if count < n:
        return nums
    
    temp_nums = nums
    temp_nums2 = temp_nums
    
    # here we remove the node at the specified index
    for i in range(0, count):
        # count = 5
        # n = 5
        # 0 = 0
        if (i == count-n-1):
            # essentially we are removing the node. this may not be the correct way,
            # but we are attempting to set it to NULL which would delete it

            ## attempting to remove node
            temp_nums.next = temp_nums.next.next
            ##

        temp_nums = temp_nums.next
    
    return nums




            


if __name__ == "__main__":
    node1 = LinkedListNode(2)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(2)
    node4 = LinkedListNode(3)
    node5 = LinkedListNode(4)  


    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Created linked list:")
    printList(node1)
    printList(removeNthNode(node1, 2))