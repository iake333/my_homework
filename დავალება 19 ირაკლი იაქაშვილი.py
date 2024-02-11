# Class for defining a single node in a linked list
class ListNode:
    # Initializes a node with a given value
    def __init__(self, value):
        self.value = value  # node value
        self.next = None  # reference to the next node


# Class for implementing a linked list
class LinkedList:
    # Initializes the linked list with a head node containing the given value
    def __init__(self, value):
        self.head = ListNode(value)
        self.length = 1

    # Appends a new node with the given value to the end of the linked list
    def append(self, value):
        current_node = self.head

        # Traverse to the end of the linked list
        while current_node.next is not None:
            current_node = current_node.next

        # Create a new node and append it to the end
        new_node = ListNode(value)
        current_node.next = new_node
        self.length += 1

    # Inserts a new node with the given value at the specified index in the linked list
    def insert(self, value, index):
        last_index = self.length - 1
        i = 0

        # Insertion at the beginning of the linked list
        if index == 0:
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            self.length += 1
